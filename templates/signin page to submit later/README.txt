RELAY AUTH — COLORLIB
====================
A standalone frontend authentication interface starter. No real backend,
account creation, mail delivery, token verification or protected session is included.

Start:
  cd relay-auth
  python3 -m http.server 8080
  Open http://localhost:8080/

Do not open the files using file://: the JavaScript uses ES modules.
Full screen list, adapter contract and integration checklist: setup.html.

Included: sign-in, registration, recovery request, check-email, reset-password,
code verification, expired-link and confirmation screens; shared styles; demo
adapter; local SVG mark; setup guide; template metadata and license.

Demo behavior:
- Use made-up details. Demo verification code: 123456.
- Password setup requires 12 characters; confirmation must match.
- Preview settings select success/rejection/network/rate-limit/expiry responses.
- Resend uses a 30-second demo cooldown. It sends no messages.
- No typed account data is written to storage or sent to a service.
- Directly visiting welcome.html does not establish an authenticated session.

Live integration:
Replace assets/auth-adapter.js with your authentication-service adapter.
Read setup.html before connecting real users. The frontend's routes and validation
must be paired with server-side session, challenge and policy enforcement.
Changing isDemo to false without implementing a real adapter fails closed.
The demo has no external packages, font requests, analytics or build step.

Design/code: Colorlib — https://colorlib.com/
License: CC BY 3.0. Keep appropriate Colorlib attribution.
