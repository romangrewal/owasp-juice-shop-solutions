## Local File Read
### Challenge: Gain read access to an arbitrary local file on the web server.

1. Log in as any user
2. Navigate to the _Request Data Erasure_ page
3. Fill in the form and send a request
4. Inspect the form parameters of the POST request
5. Use your favorite fuzzing tool to fuzz the names of the body parameters
6. Notice an unhandled `500 Internal Server Error` when a parameter `layout` is provided in the request.
    - The response body includes an error message `Error: ENOENT: no such file or directory` and the name of the file the application is trying to access: `<root_directory>/juice-shop/views/<value_of_layout_parameter>`
7. Guess or brute-force a valid filename to solve the challenge.
    - `layout=../package.json` will access the package.json file from the root server directory
