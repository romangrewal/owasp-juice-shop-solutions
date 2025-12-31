## Memory Bomb
### Challenge: Drop some explosive data into a vulnerable file-handling endpoint.

1. Log in as any user.
2. Order an item.
3. Navigate to the _Track Order_ page.
4. Observe the GET request to the rest/track-order/id route in your browser's DevTools.
5. Search for a single quote `'` as the id to throw an error.
6. Search for two single quotes `''` to throw an unexpected string error, verifying the id parameter can be enclosed in two single quotes.
7. Squeeze a MongoDB search parameter inside the single quotes (url-encoded) to solve this challenge.
    - `' || true || '` as `rest/track-order/'%20%7C%7C%20true%20%7C%7C%20'`
