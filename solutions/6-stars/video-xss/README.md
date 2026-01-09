## Video XSS
### Challenge: Embed an XSS payload \</script>\<script>alert(\`xss\`)\</script> into our promo video.

1. Search the Twitter page for OWASP Juice Shop to find posts mentioning the promotion page on both Jan 16th, 2021 and April 6th, 2019.
2. Visit the promotion page on your local instance of Juice Shop at http://\<host\>:3000/promotion.
3. Observe subtitles are enabled by default.
4. Open the Browser Inspector to observe the video loads from web root and subtitles are loaded as a .vtt file in script tags.
5. Observing the response for http://\<host\>:3000/video in the Network tab of your Browser Inspector shows the header `Content-Location: /assets/public/videos/owasp_promo.mp4`.
6. Verify the subtitle are in the same directory at http://\<host\>:3000/assets/public/videos/owasp_promo.vtt.
7. Inspect the sources of the homepage to observe in the main.js file:
    ```
    "use strict";
    (self.webpackChunkfrontend=self.webpackChunkfrontend||[])
    ```
    where `frontend` is the Angular project name.
8. Create a zip slip exploit file called `owasp_promo.vtt` with the contents ``</script><script>alert(`xss`)</script>`` under the directory structure `../../frontend/dist/frontend/assets/public/videos/owasp_promo.vtt` e.g.
    ```
    zip exploit.zip ../../frontend/dist/frontend/assets/public/videos/owasp_promo.vtt
    ```
9. Log in as any user.
10. Upload the zip slip exploit file on the complaint page.
11. Visit http://\<host\>:3000/promotion to trigger the exploit.
12. Return to the homepage to solve this challenge.
