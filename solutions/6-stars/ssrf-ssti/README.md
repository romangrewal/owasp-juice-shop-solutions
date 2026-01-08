## SSRF / SSTi
### Challenge: Request a hidden resource on server through server. / Infect the server with juicy malware by abusing arbitrary command execution.

#### Part 1
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
12. Visit the profile page.
13. Verify the server is making external requests for image files by inputting an image URL in the `Image URL` field.
    - e.g. https://placecats.com/100/100 as the `Image URL` will display a profile image of a cat with no outgoing requests from the browser (the request was made by the server).
14. Paste the destined endpoint for `juicy malware` as the `Image URL`.
15. Pasting the destined endpoint for `juicy malware` as the `Image URL` will not do anything as it needs to be called by `juicy malware` itself (on the server side).

#### Part 2
