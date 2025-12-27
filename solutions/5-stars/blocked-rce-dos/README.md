## Blocked RCE DoS
### Challenge: Perform a Remote Code Execution that would keep a less hardened application busy forever.

1. Perform manual or automated URL discovery to find Swagger API documentation hosted at http://\<host\>:3000/api-docs which describes the B2B API.
2. The given example for `orderLinesDate` indicates customer specific data format and might be allowed to contain arbitrary JSON.
3. Go back to the application, log in as any user and copy your token from the Authorization header using your browser’s DevTools.
4. Back at `/api-docs`, click Authorize and paste your token into the Value field.
5. Replace the example code with `{"orderLinesData": "(function dos() { while(true); })()"}`.
    - An insecure JSON deserialization would execute any function call defined within the JSON String
6. Click Execute.
7. If your request successfully bumped into the infinite loop protection, the challenge is marked as solved.
