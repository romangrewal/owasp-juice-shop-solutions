# OWASP Juice Shop Solutions
Penetration Testing with OWASP Juice Shop

## Installation & Setup
1. Install VirtualBox
2. Install Vagrant
3. Setup Vagrant environment for VirtualBox
4. Run `vagrant up` inside repo directory
5. Browse to http://\<vm_ip\>:3000

## Manual Solutions
1. Change to solution directory
2. See README.md file

## Python Solutions
1. Setup Python environment on localhost
```
export OWASP_JUICE_SHOP_IP_ADDRESS=<vm_ip>
export OWASP_JUICE_SHOP_PORT=3000
```
2. Change to solution directory
3. Run `python3 solution.py`

## Table of Contents
### :star: Challenges
- :heavy_check_mark: [Score Board](./solutions/1-star/score-board) ([video](https://www.youtube.com/watch?v=VEApFd5irW0)) - `Miscellaneous`
- :heavy_check_mark: [DOM XSS](./solutions/1-star/dom-xss) ([video](https://www.youtube.com/watch?v=AlVZSdyGmp8)) - `Cross Site Scripting`
- :heavy_check_mark: [Bonus Payload](./solutions/1-star/bonus-payload) ([video](https://www.youtube.com/watch?v=6tcOwMfEKI8)) - `Cross Site Scripting`
- :heavy_check_mark: [Privacy Policy](./solutions/1-star/privacy-policy) ([video](https://www.youtube.com/watch?v=zk8eLToIVdM)) - `Miscellaneous`
- :heavy_check_mark: [Bully Chatbot](./solutions/1-star/bully-chatbot) ([video](https://www.youtube.com/watch?v=W2px-Kq8a4U)) - `Prompt Injection`
- :heavy_check_mark: [Confidential Document](./solutions/1-star/confidential-document) ([video](https://www.youtube.com/watch?v=5mt7wfiU67s)) - `Sensitive Data Exposure`
- :heavy_check_mark: [Error Handling](./solutions/1-star/error-handling) ([video](https://www.youtube.com/watch?v=QzL-4pzGXkA)) - `Security Misconfiguration`
- :heavy_check_mark: [Exposed Metrics](./solutions/1-star/exposed-metrics) ([video](https://www.youtube.com/watch?v=9u9ORAc6biU)) - `Sensitive Data Exposure`
- :heavy_check_mark: [Mass Dispel](./solutions/1-star/mass-dispel) ([video](https://www.youtube.com/watch?v=LDEt2S4Jc8c)) - `Miscellaneous`
- :heavy_check_mark: [Missing Encoding](./solutions/1-star/missing-encoding) ([video](https://www.youtube.com/watch?v=HnXMTEvXNUc)) - `Improper Input Validation`
- :heavy_check_mark: [Outdated Allowlist](./solutions/1-star/outdated-allowlist) ([video](https://www.youtube.com/watch?v=5E8_2eviuZs)) - `Unvalidated Redirects`
- :heavy_check_mark: [Repetitive Registration](./solutions/1-star/repetitive-registration) ([video](https://www.youtube.com/watch?v=jLyI8Us-4IA)) - `Improper Input Validation`
- :heavy_check_mark: [Web3 Sandbox](./solutions/1-star/web3-sandbox) ([video](https://www.youtube.com/watch?v=PXLeO0r6nSk)) - `Security Misconfiguration`
- :heavy_check_mark: [Zero Stars](./solutions/1-star/zero-stars) ([video](https://www.youtube.com/watch?v=PhKB3eeTnz0)) - `Improper Input Validation`

### :star::star: Challenges
- :heavy_check_mark: [Reflected XSS](./solutions/2-stars/reflected-xss) ([video](https://www.youtube.com/watch?v=kmP3_Ywl3Cs)) - `Cross Site Scripting`
- :heavy_check_mark: [Login Admin](./solutions/2-stars/login-admin) ([video](https://www.youtube.com/watch?v=eY96fLupt1c)) - `SQL Injection`
- :heavy_check_mark: [Admin Section](./solutions/2-stars/admin-section) ([video](https://www.youtube.com/watch?v=FNNGGKT-TWw)) - `Security Misconfiguration`
- :heavy_check_mark: [Password Strength](./solutions/2-stars/password-strength) ([video](https://www.youtube.com/watch?v=B-g4P99m5ao)) - `Broken Authentication`
- :heavy_check_mark: [View Basket](./solutions/2-stars/view-basket) ([video](https://www.youtube.com/watch?v=A1weKT-p4EU)) - `Broken Access Control`
- :heavy_check_mark: [Deprecated Interface](./solutions/2-stars/deprecated-interface) ([video](https://www.youtube.com/watch?v=rVn5lklvQ6k)) - `Security Misconfiguration`
- :heavy_check_mark: [Five Star Feedback](./solutions/2-stars/reflected-xss) ([video](https://www.youtube.com/watch?v=OYkiaa9fC0Y)) - `Broken Access Control`
- :heavy_check_mark: [Login MC SafeSearch](./solutions/2-stars/login-mc-safesearch) ([video](https://www.youtube.com/watch?v=EjQ8DbrHVYE)) - `Sensitive Data Exposure`
- :heavy_check_mark: [Meta Geo Stalking](./solutions/2-stars/meta-geo-stalking) ([video](https://www.youtube.com/watch?v=xX68ZmTOKZE)) - `Sensitive Data Exposure`
- :heavy_check_mark: [NFT Takeover](./solutions/2-stars/nft-takeover) ([video](https://www.youtube.com/watch?v=Kc7eNKPXkcY)) - `Sensitive Data Exposure`
- :heavy_check_mark: [Security Policy](./solutions/2-stars/security-policy) ([video](https://www.youtube.com/watch?v=CHbeDbAIaIU)) - `Miscellaneous`
- :heavy_check_mark: [Visual Geo Stalking](./solutions/2-stars/visual-geo-stalking) ([video](https://www.youtube.com/watch?v=zOH2ejqvrRw)) - `Sensitive Data Exposure`

### :star::star::star: Challenges
- :heavy_check_mark: [Forged Feedback](./solutions/3-stars/forged-feedback) ([video](https://www.youtube.com/watch?v=z3gdHG2O4kE)) - `Broken Access Control`
- :heavy_check_mark: [Login Jim](./solutions/3-stars/login-jim) ([video](https://www.youtube.com/watch?v=gfe7meW2JOk)) - `SQL Injection`
- :heavy_check_mark: [Login Bender](./solutions/3-stars/login-bender) ([video](https://www.youtube.com/watch?v=FxJuFhFnLlg)) - `SQL Injection`
- :heavy_check_mark: [API-only XSS](./solutions/3-stars/api-only-xss) ([video](https://www.youtube.com/watch?v=pXvIgQkMac8)) - `Cross Site Scripting`
- :heavy_check_mark: [Admin Registration](./solutions/3-stars/admin-registration) ([video](https://www.youtube.com/watch?v=7aCv0DogHLc)) - `Improper Input Validation`
- :heavy_check_mark: [Bjoern's Favorite Pet](./solutions/3-stars/bjoerns-favorite-pet) ([video](https://www.youtube.com/watch?v=-5OP8VI6a7c)) - `Broken Authentication`
- :heavy_check_mark: [CAPTCHA Bypass](./solutions/3-stars/captcha-bypass) ([video](https://www.youtube.com/watch?v=eQn_AQDbA5Q)) - `Broken Anti Automation`
- :heavy_check_mark: [CSRF](./solutions/3-stars/csrf) ([video](https://www.youtube.com/watch?v=dz8jsnKgcB0)) - `Broken Access Control`
- :heavy_check_mark: [Client-side XSS Protection](./solutions/3-stars/client-side-xss-protection) ([video](https://www.youtube.com/watch?v=EtGZb_xOBoo)) - `Cross Site Scripting`
- :heavy_check_mark: [Database Schema](./solutions/3-stars/database-schema) ([video](https://www.youtube.com/watch?v=z-4_w2i96WU)) - `SQL Injection`
- :heavy_check_mark: [Deluxe Fraud](./solutions/3-stars/deluxe-fraud) ([video](https://www.youtube.com/watch?v=59I5bhGSGSc)) - `Improper Input Validation`
- :heavy_check_mark: [Forged Review](./solutions/3-stars/forged-review) ([video](https://www.youtube.com/watch?v=nVnqA3_3ds0)) - `Broken Access Control`
- :heavy_check_mark: [GDPR Data Erasure](./solutions/3-stars/gdpr-data-erasure) ([video](https://www.youtube.com/watch?v=PkD60KpQFRE)) - `Broken Authentication`
- :heavy_check_mark: [Login Amy](./solutions/3-stars/login-amy) ([video](https://www.youtube.com/watch?v=aFQbhVvUFEw)) - `Sensitive Data Exposure`

### :star::star::star::star: Challenges
- :heavy_check_mark: [Access Log](./solutions/4-stars/access-log) ([video](https://www.youtube.com/watch?v=kwxGB2PCRHQ)) - `Sensitive Data Exposure`
- :heavy_check_mark: [Allowlist Bypass](./solutions/4-stars/allowlist-bypass) ([video](https://www.youtube.com/watch?v=Zu43uOcuU_E)) - `Unvalidated Redirects`
- :heavy_check_mark: [CSP Bypass](./solutions/4-stars/csp-bypass) ([video](https://www.youtube.com/watch?v=lTdlRyUgj1U)) - `Cross Site Scripting`
- :heavy_check_mark: [Expired Coupon](./solutions/4-stars/expired-coupon) ([video](https://www.youtube.com/watch?v=oq2Ssw-TlM4)) - `Improper Input Validation`
- :heavy_check_mark: [Forgotten Developer Backup](./solutions/4-stars/forgotten-developer-backup) ([video](https://www.youtube.com/watch?v=Po3mr8TRAn4)) - `Sensitive Data Exposure`
- :heavy_check_mark: [Forgotten Sales Backup](./solutions/4-stars/forgotten-sales-backup) ([video](https://www.youtube.com/watch?v=82PGjUU3zAg)) - `Sensitive Data Exposure`
- :heavy_check_mark: [Login Bjoern](./solutions/4-stars/login-bjoern) ([video](https://www.youtube.com/watch?v=YEjIlHENpkM)) - `Broken Authentication`
- :heavy_check_mark: [Misplaced Signature File](./solutions/4-stars/misplaced-signature-file) ([video](https://www.youtube.com/watch?v=8jcSFQl3fC0)) - `Sensitive Data Exposure`
- :heavy_check_mark: [NoSQL DoS](./solutions/4-stars/nosql-dos) ([video](https://www.youtube.com/watch?v=vOumGN20eyU)) - `NoSQL Injection`
- :heavy_check_mark: [NoSQL Manipulation](./solutions/4-stars/nosql-manipulation) ([video](https://www.youtube.com/watch?v=8HXudIULZh4)) - `NoSQL Injection`
- :heavy_check_mark: [Steganography](./solutions/4-stars/steganography) ([video](https://www.youtube.com/watch?v=J9EMkvvtpJ8)) - `Security through Obscurity`
- :heavy_check_mark: [User Credentials](./solutions/4-stars/user-credentials) ([video](https://www.youtube.com/watch?v=UrIjv2lg7Tw)) - `SQL Injection`

### :star::star::star::star::star: Challenges
- :heavy_check_mark: [Blocked RCE DoS](./solutions/5-stars/blocked-rce-dos) ([video](https://www.youtube.com/watch?v=u5Ii-7KB82U)) - `Insecure Deserialization`
- :heavy_check_mark: [Change Bender's Password](./solutions/5-stars/change-benders-password) ([video](https://www.youtube.com/watch?v=lj3IIJCCvRw&t=5s)) - `Broken Authentication`
- :heavy_check_mark: [Email Leak](./solutions/5-stars/email-leak) ([video](https://www.youtube.com/watch?v=mrW7-tU94K0)) - `Sensitive Data Exposure`
- :heavy_check_mark: [Frontend Typosquatting](./solutions/5-stars/frontend-typosquatting) ([video](https://www.youtube.com/watch?v=qXrN0pxTzUU)) - `Vulnerable Components`
- :heavy_check_mark: [Kill Chatbot](./solutions/5-stars/kill-chatbot) ([video](https://www.youtube.com/watch?v=lxnF4BZUdj8)) - `Vulnerable Components`
- :heavy_check_mark: [Local File Read](./solutions/5-stars/local-file-read) - `Vulnerable Components`
- :heavy_check_mark: [Memory Bomb](./solutions/5-stars/memory-bomb) - `Insecure Deserialization`

### :star::star::star::star::star::star: Challenges
