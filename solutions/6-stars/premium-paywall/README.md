## Premium Paywall
### Challenge: Unlock Premium Challenge to access exclusive content.

1. Inspect the source of _Score Board_ page to find a comment where this challenge is defined.
    - `<!--IvLuRfBJYlmStf9XfL6ckJFngyd9LfV1JaaN/KRTPQPidTuJ7FR+D/nkWJUF+0xUF07CeCeqYfxq+OJVVa0gNbqgYkUNvn//UbE7e95C+6e+7GtdpqJ8mqm4WcPvUGIUxmGLTTAC2+G9UuFCD1DUjg==-->`
2. Run a directory brute force against web root to find http://\<host\>:3000/encryptionkeys as a browsable directory.
3. Download the `premium.key` file from this directory.
4. Use openssl with AES256 in CBC mode to decrypt the string from the comment in step 1.
    - `echo "IvLuRfBJYlmStf9XfL6ckJFngyd9LfV1JaaN/KRTPQPidTuJ7FR+D/nkWJUF+0xUF07CeCeqYfxq+OJVVa0gNbqgYkUNvn//UbE7e95C+6e+7GtdpqJ8mqm4WcPvUGIUxmGLTTAC2+G9UuFCD1DUjg==" | openssl enc -d -aes-256-cbc -K EA99A61D92D2955B1E9285B55BF2AD42 -iv 1337133713371337 -a -A`
    - This will output the plain text: `/this/page/is/hidden/behind/an/incredibly/high/paywall/that/could/only/be/unlocked/by/sending/1btc/to/us`
5. Visit http://\<host\>:3000/this/page/is/hidden/behind/an/incredibly/high/paywall/that/could/only/be/unlocked/by/sending/1btc/to/us
6. Return to the homepage to solve this challenge.
