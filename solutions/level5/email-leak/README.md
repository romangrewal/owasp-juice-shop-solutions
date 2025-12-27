## Email Leak
### Challenge: Perform an unwanted information disclosure by accessing data cross-domain.

1. Open the network tab of the browser inspector to find GET request to http://\<host\>:3000/rest/user/whoami
2. Resend this request without the Authorization header to notice it still works.
3. Add a URL parameter called "callback" to cause the API to return the content as a JavaScript fragment (JSONP) rather than a standard JSON object.
    - e.g. http://\<host\>:3000/rest/user/whoami?callback=anyone
