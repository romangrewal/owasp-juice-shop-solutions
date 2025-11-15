## Client-side XSS Protection
### Challenge: Perform a persisted XSS attack with ```<iframe src="javascript:alert(`xss`)">``` bypassing a client-side security mechanism.

1. Submit a POST request to http://\<vm_ip\>:3000/api/Users (from the register page) with ```{"email": "<iframe src=\"javascript:alert(`xss`)\">", "password": "xss"}``` as body and `application/json` as `Content-Type` header.
2. Log in to the application as admin.
3. Visit http://\<vm_ip\>:3000/#/administration.
4. An alert box with the text "xss" should appear.
5. In the network tab of your browser inspector, notice the `authentication-details` route with iframe source in the email key for the registered user
6. When you scroll to the user in the registered user list, the alert box will popup again
7. Click the "eye"-button of the iframe user (broken looking row in the Registered Users table)
8. A modal overlay dialog with the user details opens where the attack string is rendered as harmless text. (Client-side security mechanism) - The adminstration page renders xss payloads from the `authentication-details` route outside the modal dialog
