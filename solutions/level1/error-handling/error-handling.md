## Error Handling 
### Challenge: Provoke an error that is neither very gracefully nor consistently handled.

#### Error 1
* Navigate to http://\<ip\>:\<port\>/rest in the browser's address bar
* Observe an unhandled error printed to the screen that reveals the Node.js Express version


#### Error 2
* Navigate to acount login
* Login with "'" (single-quote) and anything as password
* Observe [object Object] output above "Email\*" login box, indicating code execution
* Open browser inspect
* Click on Network tab
* In the response tab for login route, observe SQLITE\_ERROR and SQL query, indicating SQL injection vulnerability
