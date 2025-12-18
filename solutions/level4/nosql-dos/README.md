## NoSQL DoS
### Challenge: Let the server sleep for some time. (It has done more than enough hard work for you)

1. Clone the OWASP Juice Shop repository from GitHub
2. On line 36 of routes/showProductReviews.ts, see
    ```
      db.reviewsCollection.find({ $where: 'this.product == ' + id })
    ```
    - where the id parameter is injectible from api route `rest/products/{id}/reviews`
3. Inject this parameter with sleep(2000)
4. Visit the homepage to solve this challenge
