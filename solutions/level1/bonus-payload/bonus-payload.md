## Bonus-Payload 
### Challenge: Use the bonus payload \<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" src="`https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/771984076&color=%23ff5500&auto_play=true&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true`">\</iframe> in the DOM XSS challenge.

* Ensure audio is enabled
* Click search icon
* Input malicious iframe into search box
* Press Enter
* Observe "Search Results" HTML is injected with Soundcloud iframe
* Observe OWASP Juice Shop Jingle is playing on the webpage
