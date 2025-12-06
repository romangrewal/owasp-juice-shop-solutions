## Access Log
### Challenge: Gain access to any access log file of the server.

1. Visit the FTP folder at `http://<vm_ip>:3000/ftp`
2. See the `incident-support.kdbx` file
    - This file indicates web access from a support team
3. Using ffuf, check to see if there are any files in `support` directory, verifying existance of `support` directory and `logs` file.

        ffuf -w directory_wordlists.txt -u http://<vm_ip>:3000/support/FUZZ -fs 75002

4. Download `access.log.DATE` file.
5. Visit home page to solve this challenge.
