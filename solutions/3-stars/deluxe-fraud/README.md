## Deluxe Fraud
### Challenge: Obtain a Deluxe Membership without paying for it.

1. Log in to the application as any user.
2. Copy the Bearer Token from the Authorization header from any HTTP request submitted via browser.
3. Submit a POST request to http://\<vm_ip\>:3000/rest/deluxe-membership with
    - ```{"paymentMode":""}``` as body 
    - and `application/json` as `Content-Type` and the Bearer token you copied from the browser as the Authorization header
4. Visit http://\<vm_ip\>:3000 to solve this challenge.
