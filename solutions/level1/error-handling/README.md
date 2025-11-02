## Error Handling 
### Challenge: Provoke an error that is neither very gracefully nor consistently handled.

#### Error 1
1. Navigate to http://\<ip\>:\<port\>/rest in the browser's address bar
2. Observe an unhandled error printed to the screen that reveals the Node.js Express version


#### Error 2
1. Navigate to acount login
2. Login with "'" (single-quote) and anything as password
3. Observe [object Object] output above "Email\*" login box, indicating code execution
4. Open browser inspect
5. Click on Network tab
6. In the response tab for login route, observe SQLITE\_ERROR and SQL query, indicating SQL injection vulnerability
