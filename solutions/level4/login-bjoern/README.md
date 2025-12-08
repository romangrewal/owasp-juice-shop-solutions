## Login Bjoern
### Challenge: Log in with Bjoern's Gmail account without previously changing his password, applying SQL Injection, or hacking his Google account.

1. Search for string `oauth` in `main.js`
2. In method `userService.oauthLogin()` you will see `password: btoa(n.email.split("").reverse().join(""))`
  - `btoa()` is a default function to encode strings into Base64
  - `email.split("").reverse().join("")` reverses the email string
3. Base64 encode `moc.liamg@hcinimmik.nreojb` to login with
  - Email: `bjoern.kimminich@gmail.com` and
  - Password: `bW9jLmxpYW1nQGhjaW5pbW1pay5ucmVvamI=`
