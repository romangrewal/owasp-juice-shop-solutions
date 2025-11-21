## CSRF
### Challenge: Change the name of a user by performing Cross-Site Request Forgery from another origin.

1. Download and old version of Firefox (96.x) or Chrome (79.x) which sets cookies with `SameSite=None` by default.
2. Login with any user account. This user is going to be the victim of the CSRF attack.
3. Navigate to http://htmledit.squarefree.com in the same browser. It is intentional that the site is accessed without TLS, as otherwise there might be issues with the mixed-content policy of the browser.
4. Paste the following HTML fragment, which contains a self-submitting HTML form:
  - ```
      <form action="http://localhost:3000/profile" method="POST">
        <input name="username" value="CSRF"/>
        <input type="submit"/>
      </form>
      <script>document.forms[0].submit();</script>
    ```
  - The attack is performed immediately. You will see an error message or a blank page in the lower frame, because even though the online HTML editor is allowed to send requests to Juice Shop, it is not permitted to embed the response.

