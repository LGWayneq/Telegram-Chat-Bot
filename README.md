# Telegram Chat Bot
 
A simple chat bot using Telegram API. The bot will reply using randomly selected stickers from stickerdata.py and phrases in the replylist field.
I also added an extra response for whenever any food is mentioned.

The bot is also able to send a randomly selected picture from a "Pics" folder in the same directory.

<h2>Guide for Users</h2>
1. Create new bot using https://telegram.me/BotFather<br>
2. Input new bot token into TOKEN field in chatbot.py<br>
3. Creating hosting service using any platform (I used Heroku)<br>
4. Input host url into APP_NAME field in chatbot.py<br>
5. Run program<br>
6. Feel free to add new phrases/stickers or other functions to the bot


<h2>Bot Functions</h2>
/pics       - Bot will send a random photo
/sticker     - Bot will send a random sticker
/help or /start      - Show the help message
