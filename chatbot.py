import logging
import os
from random import randint
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from telegram import Bot, ReplyKeyboardMarkup, KeyboardButton
import pathlib
import stickerdata

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

availablePorts = ["443","80","88","8443"]
PORT = int(os.environ.get('PORT', "'8443'"))

TOKEN = ""
APP_NAME = ""
bot = Bot(TOKEN)

replylist = ["Love you <3", "You are my cutie pie"]
keyboardlist = ["/ourpics","/sticker","/help"]

picspath = pathlib.Path.cwd().joinpath('Pics')
picslist = [x for x in picspath.glob("*")]

with open("food.txt","r") as foodfile:
    foodlist = foodfile.read().split('\n')
    foodfile.close()
    
with open("startmessage.txt", "r") as startfile:
    startmessage = startfile.read()
    startfile.close()

def start(update, context):
    chatid = update.message.chat_id
    bot.send_message(chat_id = chatid, text = startmessage, reply_markup = createKeyboard())
    chatid = update.message.chat_id

def sticker(update, context):
    update.message.reply_sticker(sticker = stickerdata.randompenguinid(), reply_markup = createKeyboard())    
    chatid = update.message.chat_id

def reply(update, context):
    chatid = update.message.chat_id
    chatmessage = update.message.text
    if any(x in chatmessage for x in foodlist):
        update.message.reply_sticker(sticker = stickerdata.fooddanceid)
        bot.send_message(chat_id = chatid, text = "yummy in my tummy", reply_markup = createKeyboard())
    else:
        penguin(update,context)
        bot.send_message(chat_id=chatid, text = replylist[randint(0,len(replylist)-1)], reply_markup = createKeyboard())    
        

def ourpics(update, context):
    photoidx = randint(0,len(picslist)-1)
    update.message.reply_photo(photo=open("{}".format(picslist[photoidx]), 'rb'), reply_markup = createKeyboard())
    chatid = update.message.chat_id

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def createKeyboard():
  button_list = []
  for each in keyboardlist:
     button_list.append(KeyboardButton(each, callback_data = each))
  reply_markup=ReplyKeyboardMarkup(build_menu(button_list,n_cols=1)) #n_cols = 1 is for single column and mutliple rows
  return reply_markup

def build_menu(buttons,n_cols,header_buttons=None,footer_buttons=None):
  menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
  if header_buttons:
    menu.insert(0, header_buttons)
  if footer_buttons:
    menu.append(footer_buttons)
  return menu

def main():
    updater = Updater(
        TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    dp.add_handler(CommandHandler(["start","help"], start))
    dp.add_handler(CommandHandler("sticker", sticker))
    dp.add_handler(CommandHandler(["photo", "photos", "pics", "pic", "ourpics", "ourpic"], ourpics))
 

    dp.add_handler(MessageHandler(Filters.text, reply))


    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN)
    # updater.bot.set_webhook(url=settings.WEBHOOK_URL)
    updater.bot.set_webhook(APP_NAME + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
