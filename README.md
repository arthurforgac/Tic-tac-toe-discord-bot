# PROJECT SETUP

Install the required packages:
```
pip install -r requiremenets.txt
```
To set up the bot create a Discord application over on https://discord.com/developers/applications and log in with your account.

1. Create a bot in the application interface
2. Head over to OAuth2 -> Url generator
3. Select option "bot"
4. A URL will appear at the bottom of the page, which you can open in browser and select the server, where you want the bot to join
5. Back in the application interface, click on "Bot" in the sidebar
6. Customize your bot to your liking and hit the "Reset token" button
7. Replace the "TOKEN_GOES_HERE" string at the bottom of commands.py file with the new token

##Description
This is a simple Discord bot, which plays text-based tic-tac-toe.