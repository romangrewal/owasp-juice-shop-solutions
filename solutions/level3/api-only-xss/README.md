## API-only XSS
### Challenge: Perform a persisted XSS attack with `<iframe src="javascript:alert('xss')">` without using the frontend application at all.

1. Log in to the application as any user.
2. Copy the Bearer Token from the Authorization header from any HTTP request submitted via browser.
3. Submit a POST request to http://\<vm_ip\>:3000/api/Products with
  - ```{"name": "XSS", "description": "<iframe src=\"javascript:alert('xss')\">", "price": 47.11}``` as body 
  - and `application/json` as `Content-Type` and the Bearer token you copied from the browser as the Authorization header
4. Visit http://\<vm_ip\>:3000/#/search.
5. Click on the product listing you added via the api request
6. An alert box with the text "xss" should appear.
