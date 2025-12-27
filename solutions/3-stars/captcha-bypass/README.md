## CAPTCHA Bypass
### Challenge: Submit 10 or more customer feedbacks within 20 seconds.

1. Visit http://\<vm_ip\>:3000/#/contact.
2. Open the Network tab of your browser inspector.
3. Fill out the form normally and submit it.
4. Check POST request to `/api/Feedbacks` route to find JSON body:
  - ```{comment: "Hello", rating: 1, captcha: "320", captchaId: 18}```
5. Verify captcha parameters can be pinned by sending another feedback request with the captcha parameters set to be the same as the previous values.
6. Write script with a 10-iteration loop that sends the POST request to `/api/Feedbacks` with the pinned captcha values.
