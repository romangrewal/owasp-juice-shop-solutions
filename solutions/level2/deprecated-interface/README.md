## Deprecated Interface
### Challenge: Use a deprecated B2B interface that was not properly shut down.

1. Log in to the application as any user
2. Navigate to Complaint page in left hand menu
3. Upload file type other than visually allowed PDF & ZIP
4. Observe UI error message - "Forbidden file type"
5. Search for declaration of the file upload in main.js with `zip` keyword
6. Observe `application/xml` and `text/xml` along with the expected PDF and ZIP types in `allowedMimeType` array
7. Upload any arbitrary XML file (<100KB)
8. Submit form to complete this challenge
9. Observe 410 (Gone) in JavaScript Console and error page in Network tab
