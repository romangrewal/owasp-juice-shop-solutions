## Arbitrary File Write
### Challenge: Overwrite the Legal Information file.

1. Log in as any user
2. Prepare a ZIP file (on Linux) with `zip exploit.zip ../../ftp/legal.md`.
    - When unzipped by back-end processing, this directory structure will overwrite the legal.md file in the ftp folder.
4. Navigate to the _Complaint_ page.
5. Type in any message and attach your ZIP file.
6. Click Submit to solve this challenge.
