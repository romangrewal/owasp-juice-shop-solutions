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
- :heavy_check_mark: [Score Board](./solutions/level1/score-board) ([video](https://www.youtube.com/watch?v=VEApFd5irW0)) - `Miscellaneous`
- :heavy_check_mark: [DOM XSS](./solutions/level1/dom-xss) ([video](https://www.youtube.com/watch?v=AlVZSdyGmp8)) - `Cross Site Scripting`
- :heavy_check_mark: [Bonus Payload](./solutions/level1/bonus-payload) ([video](https://www.youtube.com/watch?v=6tcOwMfEKI8)) - `Cross Site Scripting`
- :heavy_check_mark: [Privacy Policy](./solutions/level1/privacy-policy) ([video](https://www.youtube.com/watch?v=zk8eLToIVdM)) - `Miscellaneous`
- :heavy_check_mark: [Bully Chatbot](./solutions/level1/bully-chatbot) ([video](https://www.youtube.com/watch?v=W2px-Kq8a4U)) - `Prompt Injection`
- :heavy_check_mark: [Confidential Document](./solutions/level1/confidential-document) ([video](https://www.youtube.com/watch?v=5mt7wfiU67s)) - `Sensitive Data Exposure`
- :heavy_check_mark: [Error Handling](./solutions/level1/error-handling) ([video](https://www.youtube.com/watch?v=QzL-4pzGXkA)) - `Security Misconfiguration`
- :heavy_check_mark: [Exposed Metrics](./solutions/level1/exposed-metrics) ([video](https://www.youtube.com/watch?v=9u9ORAc6biU)) - `Sensitive Data Exposure`
- :heavy_check_mark: [Mass Dispel](./solutions/level1/mass-dispel) ([video](https://www.youtube.com/watch?v=LDEt2S4Jc8c)) - `Miscellaneous`
- :heavy_check_mark: [Missing Encoding](./solutions/level1/missing-encoding) ([video](https://www.youtube.com/watch?v=HnXMTEvXNUc)) - `Improper Input Validation`
- :heavy_check_mark: [Outdated Allowlist](./solutions/level1/outdated-allowlist) ([video](https://www.youtube.com/watch?v=5E8_2eviuZs)) - `Unvalidated Redirects`
- :heavy_check_mark: [Repetitive Registration](./solutions/level1/repetitive-registration) ([video](https://www.youtube.com/watch?v=jLyI8Us-4IA)) - `Improper Input Validation`
- :heavy_check_mark: [Web3 Sandbox](./solutions/level1/web3-sandbox) ([video](https://www.youtube.com/watch?v=PXLeO0r6nSk)) - `Security Misconfiguration`
- :heavy_check_mark: [Zero Stars](./solutions/level1/zero-stars) ([video](https://www.youtube.com/watch?v=PhKB3eeTnz0)) - `Improper Input Validation`

### :star::star: Challenges
- :heavy_check_mark: [Reflected XSS](./solutions/level2/reflected-xss) ([video](https://www.youtube.com/watch?v=kmP3_Ywl3Cs)) - `Cross Site Scripting`
- :heavy_check_mark: [Login Admin](./solutions/level2/login-admin) ([video](https://www.youtube.com/watch?v=eY96fLupt1c)) - `SQL Injection`
- :heavy_check_mark: [Admin Section](./solutions/level2/admin-section) ([video](https://www.youtube.com/watch?v=FNNGGKT-TWw)) - `Security Misconfiguration`
- :heavy_check_mark: [Password Strength](./solutions/level2/password-strength) ([video](https://www.youtube.com/watch?v=B-g4P99m5ao)) - `Broken Authentication`
- :heavy_check_mark: [View Basket](./solutions/level2/view-basket) ([video](https://www.youtube.com/watch?v=A1weKT-p4EU)) - `Broken Access Control`
- :heavy_check_mark: [Deprecated Interface](./solutions/level2/deprecated-interface) ([video](https://www.youtube.com/watch?v=rVn5lklvQ6k)) - `Security Misconfiguration`
- :heavy_check_mark: [Five Star Feedback](./solutions/level2/reflected-xss) ([video](https://www.youtube.com/watch?v=OYkiaa9fC0Y)) - `Broken Access Control`
- :heavy_check_mark: [Login MC SafeSearch](./solutions/level2/login-mc-safesearch) ([video](https://www.youtube.com/watch?v=EjQ8DbrHVYE)) - `Sensitive Data Exposure`
- :heavy_check_mark: [Meta Geo Stalking](./solutions/level2/meta-geo-stalking) ([video](https://www.youtube.com/watch?v=xX68ZmTOKZE)) - `Sensitive Data Exposure`
- :heavy_check_mark: [NFT Takeover](./solutions/level2/nft-takeover) ([video](https://www.youtube.com/watch?v=Kc7eNKPXkcY)) - `Sensitive Data Exposure`
- :heavy_check_mark: [Security Policy](./solutions/level2/security-policy) ([video](https://www.youtube.com/watch?v=CHbeDbAIaIU)) - `Miscellaneous`
- :heavy_check_mark: [Visual Geo Stalking](./solutions/level2/visual-geo-stalking) ([video](https://www.youtube.com/watch?v=zOH2ejqvrRw)) - `Sensitive Data Exposure`

### :star::star::star: Challenges
- :heavy_check_mark: [Forged Feedback](./solutions/level3/forged-feedback) ([video](https://www.youtube.com/watch?v=z3gdHG2O4kE)) - `Broken Access Control`
- :heavy_check_mark: [Login Jim](./solutions/level3/login-jim) ([video](https://www.youtube.com/watch?v=gfe7meW2JOk)) - `SQL Injection`
- :heavy_check_mark: [Login Bender](./solutions/level3/login-bender) ([video](https://www.youtube.com/watch?v=FxJuFhFnLlg)) - `SQL Injection`
- :heavy_check_mark: [API-only XSS](./solutions/level3/api-only-xss) ([video](https://www.youtube.com/watch?v=pXvIgQkMac8)) - `Cross Site Scripting`
- :heavy_check_mark: [Admin Registration](./solutions/level3/admin-registration) ([video](https://www.youtube.com/watch?v=7aCv0DogHLc)) - `Improper Input Validation`
- :heavy_check_mark: [Bjoern's Favorite Pet](./solutions/level3/bjoerns-favorite-pet) ([video](https://www.youtube.com/watch?v=-5OP8VI6a7c)) - `Broken Authentication`
- :heavy_check_mark: [CAPTCHA Bypass](./solutions/level3/captcha-bypass) ([video](https://www.youtube.com/watch?v=eQn_AQDbA5Q)) - `Broken Anti Automation`
- :heavy_check_mark: [CSRF](./solutions/level3/csrf) ([video](https://www.youtube.com/watch?v=dz8jsnKgcB0)) - `Broken Access Control`
- :heavy_check_mark: [Client-side XSS Protection](./solutions/level3/client-side-xss-protection) ([video](https://www.youtube.com/watch?v=EtGZb_xOBoo)) - `Cross Site Scripting`
- :heavy_check_mark: [Database Schema](./solutions/level3/database-schema) ([video](https://www.youtube.com/watch?v=z-4_w2i96WU)) - `SQL Injection`
- :heavy_check_mark: [Deluxe Fraud](./solutions/level3/deluxe-fraud) - `Improper Input Validation`
- :heavy_check_mark: [Forged Review](./solutions/level3/forged-review) - `Broken Access Control`
- :heavy_check_mark: [GDPR Data Erasure](./solutions/level3/gdpr-data-erasure) - `Broken Authentication`
- :heavy_check_mark: [Login Amy](./solutions/level3/login-amy) - `Sensitive Data Exposure`

### :star::star::star::star: Challenges
- :heavy_check_mark: [Access Log](./solutions/level4/access-log) - `Sensitive Data Exposure`

### :star::star::star::star::star: Challenges
### :star::star::star::star::star::star: Challenges
