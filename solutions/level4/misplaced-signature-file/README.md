## Misplaced Signature File
### Challenge: Access a misplaced SIEM signature file.

1. Visit the ftp folder
2. Open `suspicious_errors.yml` directly to view error message `Only .md and .pdf files are allowed!`
3. Use a Poison Null Byte (`%00`) with the `%` character URL-encoded to `%25` and the md or pdf extension to view the file in your browser
    ```
      http://instance_ip:3000/ftp/suspicious_errors.yml%2500.md
    ```
4. Visit homepage to solve this challenge
