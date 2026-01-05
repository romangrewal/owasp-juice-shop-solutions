## Successful RCE DoS
### Challenge: Perform a Remote Code Execution that occupies the server for a while without using infinite loops.

1. Perform manual or automated URL discovery to find Swagger API documentation hosted at http://\<host\>:3000/api-docs which describes the B2B API.
2. The given example for `orderLinesDate` indicates customer specific data format and might be allowed to contain arbitrary JSON.
3. Go back to the application, log in as any user and copy your token from the Authorization header using your browser’s DevTools.
4. Back at `/api-docs`, click Authorize and paste your token into the Value field.
5. Replace the example code with `{"orderLinesData": "/((a+)+)b/.test('aaaaaaaaaaaaaaaaaaaaaaaaaaaaa')"}`.
    - An insecure JSON deserialization would execute any function call defined within the JSON String. This will trigger a very costly Regular Expression test once executed.
6. Click Execute.
7. The server will eventually respond with a `503` status and an error stating `Sorry, we are temporarily not available! Please try again later.`
8. Return to the homepage to solve this challenge.
