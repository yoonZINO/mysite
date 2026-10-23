import { authenticate, isDemo } from './auth-adapter.js';
const scenario = () => isDemo ? (document.querySelector('#scenario')?.value || 'success') : 'success';
if (!isDemo) document.querySelectorAll('.preview-tools,.demo-next,.demo-badge').forEach(e => e.hidden = true);
const notice = document.querySelector('.notice');
if (new URLSearchParams(location.search).get('notice') === 'reset' && notice) {
  notice.hidden = false;
  notice.textContent = isDemo ? 'Demo reset completed. Try signing in next.' : 'Password updated. Sign in with your new password.';
}
for (const button of document.querySelectorAll('[data-reveal]')) {
  const input = document.getElementById(button.dataset.reveal);
  input.dataset.password = 'true';
  button.addEventListener('click', () => {
    const show = input.type === 'password';
    input.type = show ? 'text' : 'password';
    button.textContent = show ? 'Hide' : 'Show';
    button.setAttribute('aria-pressed', String(show));
    button.setAttribute('aria-label', `${show ? 'Hide' : 'Show'} ${input.labels[0].textContent.toLowerCase()}`);
  });
}
function fieldError(input, message) {
  input.setAttribute('aria-invalid', String(Boolean(message)));
  document.getElementById(`${input.id}-error`).textContent = message;
}
function validate(form) {
  let first;
  for (const input of form.querySelectorAll('input')) {
    let message = '';
    if (!input.value.trim()) message = `Enter ${input.labels[0].textContent.toLowerCase()}.`;
    else if (input.validity.typeMismatch) message = 'Enter a valid email address.';
    else if (input.minLength > 0 && input.value.length < input.minLength) message = `Use at least ${input.minLength} characters.`;
    else if (input.validity.patternMismatch) message = 'Enter all six digits.';
    if (input.name === 'confirm' && input.value !== form.elements.password.value) message = 'Your passwords do not match.';
    fieldError(input, message);
    if (message && !first) first = input;
  }
  first?.focus();
  return !first;
}
function friendlyError(error, operation) {
  if (error.code === 'NETWORK') return 'We couldn’t connect. Please try again.';
  if (error.code === 'RATE_LIMITED') return 'Too many attempts. Please wait before trying again.';
  if (error.code === 'EXPIRED') return 'This code has expired. Request a new code and try again.';
  if (operation === 'verifyCode') return 'That code didn’t match. Check all six digits and try again.';
  if (operation === 'signIn') return 'We couldn’t sign you in with those details. Check them and try again.';
  return 'We couldn’t complete that request. Please try again.';
}
const routes = { signIn: 'welcome.html', signUp: 'verify.html', requestReset: 'check-email.html', resetPassword: 'index.html?notice=reset', verifyCode: 'welcome.html' };
for (const form of document.querySelectorAll('form[data-operation]')) {
  let busy = false;
  form.querySelector('[type=submit]').disabled = false;
  form.addEventListener('input', event => {
    if (event.target.matches('input')) fieldError(event.target, '');
  });
  form.addEventListener('submit', async event => {
    event.preventDefault();
    if (busy || !validate(form)) return;
    const button = form.querySelector('[type=submit]');
    const errorBox = form.querySelector('.form-error');
    const status = form.querySelector('.form-status');
    const operation = form.dataset.operation;
    busy = true; button.disabled = true; form.setAttribute('aria-busy', 'true');
    errorBox.hidden = true; status.textContent = 'Please wait…';
    const data = Object.fromEntries(new FormData(form));
    delete data.confirm;
    try {
      await authenticate(operation, data, { scenario: scenario() });
      form.reset();
      location.assign(routes[operation]);
    } catch (error) {
      if (error.code === 'EXPIRED' && operation === 'resetPassword') {
        form.reset(); location.assign('expired-link.html'); return;
      }
      errorBox.textContent = friendlyError(error, operation);
      errorBox.hidden = false; status.textContent = ''; errorBox.focus();
    } finally {
      // Release references; never persist passwords, codes or account data.
      for (const key of Object.keys(data)) delete data[key];
      busy = false; button.disabled = false; form.removeAttribute('aria-busy');
    }
  });
}
for (const button of document.querySelectorAll('[data-resend]')) {
  const status = document.querySelector('[data-resend-status]');
  const countdown = document.querySelector('[data-countdown]');
  let timer;
  button.addEventListener('click', async () => {
    button.disabled = true; status.textContent = 'Please wait…';
    try {
      await authenticate(button.dataset.resend === 'reset' ? 'resendReset' : 'resendVerification', {}, { scenario: scenario() });
      status.textContent = isDemo ? 'Demo resend complete. No message was sent.' : 'If eligible, a new message will be sent.';
      const until = Date.now() + 30000;
      const tick = () => {
        const remaining = Math.max(0, Math.ceil((until - Date.now()) / 1000));
        countdown.textContent = remaining ? `Try again in ${remaining}s` : '';
        if (!remaining) { clearInterval(timer); button.disabled = false; }
      };
      tick(); timer = setInterval(tick, 500);
    } catch (error) { status.textContent = friendlyError(error, 'resend'); button.disabled = false; }
  });
  window.addEventListener('pagehide', () => clearInterval(timer), { once: true });
}
