## Admin Registration
### Challenge: Register as a user with administrator privileges.

1. Submit a POST request to the registration route http://\<vm_ip\>:3000/api/Users with:
   - `{"email":"admin@test.com","password":"admin","role":"admin"}` as body
   - and `application/json` as `Content-Type`
2. Visit the application's web UI to complete this challenge
