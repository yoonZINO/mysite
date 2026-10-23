/** DEMO ONLY. Replace these methods with your own service integration.
 * Never implement real authentication or token validation in browser code.
 * Methods resolve only on a successful server response; reject with an Error
 * whose code is NETWORK, RATE_LIMITED, EXPIRED, or REJECTED otherwise.
 */
export const isDemo = true;
export async function authenticate(operation, data, { scenario = 'success' } = {}) {
  if (!isDemo) throw Object.assign(new Error('Replace the demo adapter before enabling live mode'), { code: 'NOT_CONFIGURED' });
  await new Promise(resolve => setTimeout(resolve, 650));
  const codes = { network: 'NETWORK', rate: 'RATE_LIMITED', expired: 'EXPIRED', rejected: 'REJECTED' };
  if (codes[scenario]) throw Object.assign(new Error('Simulated response'), { code: codes[scenario] });
  if (operation === 'verifyCode' && data.code !== '123456') {
    throw Object.assign(new Error('Invalid demo code'), { code: 'REJECTED' });
  }
  // No credentials are sent, stored or compared with real account data.
  return { ok: true };
}
