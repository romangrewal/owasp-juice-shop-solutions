## Kill Chatbot
### Challenge: Permanently disable the support chatbot so that it can no longer answer customer queries.

1. Visit the source code for the chatbot at https://github.com/juice-shop/juicy-chat-bot
2. Notice that user messages are processed inside a VM context, with a function called `process`.
3. In index.js, see the `addUser` function:
    - The command `this.factory.run(users.addUser("${token}", "${name}"))` is equivalent to an eval statement inside the VM context.
4. Exploit by including `"` and `)` in one’s username. If one sets their username to `admin"); processQuery=null; users.addUser("1337", "test`, the final statement that gets executed would be
    ```
    users.addUser("token", "admin");
    process = null;
    users.addUser("1337", "test")
    ```
5. Ask the bot one more question to demonstrate the successful exploit and complete this challenge.
