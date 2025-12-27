## Allowlist Bypass
### Challenge: Enforce a redirect to a page you are not supposed to redirect to.

1. Pick one of the redirect links in the application, e.g. `http://<vim_ip>:3000/redirect?to=https://github.com/juice-shop/juice-shop` from the GitHub-button in the navigation bar.
2. Trying to redirect to some unrecognized URL fails due to allowlist validation with `406 Error: Unrecognized target URL for redirect.`
3. Craft a redirect URL so that the target-URL in `?to=` comes with a parameter containing a URL from the allowlist, e.g. `http://<vm_ip>:3000/redirect?to=http://kimminich.de?pwned=https://github.com/juice-shop/juice-shop`
4. Visit the homepage to solve this challenge
