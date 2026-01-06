## Forged Coupon
### Challenge: Forge a coupon code that gives you a discount of at least 80%.

1. Log in as any user.
2. Visit the ftp folder.
3. Download the `package.json.bak` file with a null byte injection
4. Scan this file for crypto and hashing libraries e.g. `hashids`, `jsonwebtoken`, and `z85`.
5. Choosing `z85` as the algorithm, visit https://www.npmjs.com/package/z85.
6. Check the _Dependents_ tab for `z85-cli`.
7. Install `z85-cli` with `npm install -g z85-cli`.
8. Check the official Juice Shop Twitter account https://twitter.com/owasp_juiceshop for the valid coupon code, pEw8oh.u)v, posted on October 13th, 2017.
9. Decrypting this code with `z85 -d "pEw8oh.u)v"` returns `OCT17-50`.
10. Encrypt a code valid for the current month with 80% or more discount, e.g. `z85 -e JAN26-80` which returns `n<Michz3)x`.
11. Add some items to your basket.
12. Proceed to _Checkout_.
13. Redeem the coupon in the _Add a coupon_ section.
14. Proceed to the next page.
15. Click the _Place your order and pay_ button to solve this challenge.
