## Forged Review
### Challenge: Post a product review as another user or edit any user's existing review.

1. Log in to the application as any user different than user you are forging the review with.
2. Copy the Bearer Token from the Authorization header from any HTTP request submitted via browser.
3. Submit a POST request to http://\<vm_ip\>:3000/rest/product/\<product_num\>/reviews with
    - ```{"message":"Bad review", "author":"<forged_user_email>"}``` as body 
    - and `application/json` as `Content-Type` and the Bearer token you copied from the browser as the Authorization header
4. Visit http://\<vm_ip\>:3000/ to solve this challenge.
