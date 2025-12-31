## Supply Chain Attack
### Challenge: Inform the development team about a danger to some of their credentials. (Send them the URL of the original report or an assigned CVE or another identifier of this vulnerability)

1. Visit the ftp folder
2. Use a Poison Null Byte (`%00`) with the `%` character URL-encoded to `%25` to download the `package.json.bak` file as a md or pdf file
    ```
      http://instance_ip:3000/ftp/package.json.bak%2500.md
    ```
    - This will solve the `Access a developer’s forgotten backup file` challenge
3. Go through the list of devDependencies and perform research on vulnerabilities in them until you find the `eslint-scope` module.
4. Visit `http://status.npmjs.org/incidents/dn7c1fgrr7ng` for the pinned version `3.7.2`.
5. From the incident report on NPM, click on the original report of the vulnerability: `https://github.com/eslint/eslint-scope/issues/39`.
6. Visit the customer feedback page.
7. Submit your feedback with https://github.com/eslint/eslint-scope/issues/39 in the comment to solve this challenge.
