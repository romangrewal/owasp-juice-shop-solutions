## Change Bender's Password
### Challenge: Change Bender's password into slurmCl4ssic without using SQL Injection or Forgot Password.

1. Log in as any user.
2. Use Postman, cURL, Burp Suite, or your favorite tool to probe the GET parameters of `/rest/user/change-password` on various inputs:
    - current = `String`
    - new = `String`
    - repeat = `String`
3. Conclude that /rest/user/change-password only needs the new password fields to return `200` success
    - new = `String`
    - repeat = `String`
4. Log in with Bender's account using SQL injection.
    - Email `bender@juice-sh.op'--` and any Password
5. Craft a GET request with Bender’s Authorization header token to `/rest/user/change-password` and "slurmCl4ssic" as the new and repeat password
    - new = slurmCl4ssic
    - repeat = slurmCl4ssic
