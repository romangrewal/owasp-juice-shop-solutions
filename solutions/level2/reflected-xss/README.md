## Reflected XSS
### Challenge: Perform a reflected XSS attack with ``<iframe src="javascript:alert(`xss`)">``.

1. Log in to the application as any user
2. Order some items
3. Click on "Your Basket"
4. Checkout your items
5. Add a new address if you have to
6. Click "Continue"
7. Select a delivery speed
8. Click "Continue"
9. Add a new credit card if you have to
10. Click "Continue"
11. Proceed with payment
12. Navigate to "Order History" under Account -> Orders & Payment menu
13. Click on Track Order icon
14. Observe order id in both browser URL GET request and HTML "Search Results", indicating xss injection vector
15. Replace order id in browser with url encoded payload 
16. Observe reflected xss vulnerability
