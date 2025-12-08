## Forgotten Sales Backup
### Challenge: Access a salesman's forgotten backup file.

1. Visit the ftp folder
2. Open `coupons_2013.md.bak` directly to view error message `Only .md and .pdf files are allowed!`
3. Use a Poison Null Byte (`%00`) with the `%` character URL-encoded to `%25` to download the file as a md or pdf file
    ```
      http://instance_ip:3000/ftp/coupons_2013.md.bak%2500.md
    ```
4. Visit homepage to solve this challenge
