## Reflected XSS
### Challenge: Perform a reflected XSS attack with `<iframe src="javascript:alert(\`xss\`)">`.

* Log in to the application as any user
* Order some items
* Click on "Your Basket"
* Checkout your items
* Add a new address if you have to
* Click "Continue"
* Select a delivery speed
* Click "Continue"
* Add a new credit card if you have to
* Click "Continue"
* Proceed with payment
* Navigate to "Order History" under Account -> Orders & Payment menu
* Click on Track Order icon
* Observe order id in both browser URL GET request and HTML "Search Results", indicating xss injection vector
* Replace order id in browser with url encoded payload 
* Observe reflected xss vulnerability
