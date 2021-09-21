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

TOKEN = "1882181530:AAGiIvZactC6-V86vrzEAPa8S5exO9SoDu0"
APP_NAME = "https://huitingbot.herokuapp.com/"
bot = Bot(TOKEN)

ziweiid = 245334087
huitingid = 246883509
replylist = ["Love you babe <3", "You are my cutie piee", "jiggle jiggle jiggle", "my bby is the besttt", "pingu miss jiejie"]
keyboardlist = ["/ourpics","/ziweipics","/pingu","/buttshake", "/help"]

picspath = pathlib.Path.cwd().joinpath('Pics')
picslist = [x for x in picspath.glob("*")]

ziweipath = pathlib.Path.cwd().joinpath('Ziwei Pics')
ziweipicslist = [x for x in ziweipath.glob("*")]

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
    if chatid == huitingid:
        bot.send_message(chat_id = ziweiid, text = "from huiting: /help") #see huiting messages

def pingupat(update, context):
    update.message.reply_sticker(sticker = stickerdata.pingupatid, reply_markup = createKeyboard())
    chatid = update.message.chat_id
    if chatid == huitingid:
        bot.send_message(chat_id = ziweiid, text = "from huiting: /pingupat") #see huiting messages

def pingu(update, context):
    update.message.reply_sticker(sticker = stickerdata.randompinguid(), reply_markup = createKeyboard())    
    chatid = update.message.chat_id
    if chatid == huitingid:
        bot.send_message(chat_id = ziweiid, text = "from huiting: /pingu") #see huiting messages
     
def buttshake(update, context):
    update.message.reply_sticker(sticker = stickerdata.buttshakeid, reply_markup = createKeyboard())
    chatid = update.message.chat_id
    if chatid == huitingid:
        bot.send_message(chat_id = ziweiid, text = "from huiting: /buttshake") #see huiting messages

def reply(update, context):
    chatid = update.message.chat_id
    chatmessage = update.message.text
    if chatid == huitingid:
        bot.send_message(chat_id = ziweiid, text = "from huiting: " + chatmessage) #see huiting messages
    if any(x in chatmessage for x in foodlist):
        update.message.reply_sticker(sticker = stickerdata.fooddanceid)
        bot.send_message(chat_id = chatid, text = "yummy in my tummyy", reply_markup = createKeyboard())
    else:
        pingu(update,context)
        bot.send_message(chat_id=chatid, text = replylist[randint(0,len(replylist)-1)], reply_markup = createKeyboard())    
        

def ourpics(update, context):
    photoidx = randint(0,len(picslist)-1)
    update.message.reply_photo(photo=open("{}".format(picslist[photoidx]), 'rb'), reply_markup = createKeyboard())
    chatid = update.message.chat_id
    if chatid == huitingid:
        bot.send_message(chat_id = ziweiid, text = "from huiting: /ourpics") #see huiting messages
    
def ziweipics(update, context):
    photoidx = randint(0,len(ziweipicslist)-1)
    update.message.reply_photo(photo=open("{}".format(ziweipicslist[photoidx]), 'rb'), reply_markup = createKeyboard())
    chatid = update.message.chat_id
    if chatid == huitingid:
        bot.send_message(chat_id = ziweiid, text = "from huiting: /ziweipics") #see huiting messages

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

def sendtohuitingprompt(update, context):
    bot.send_message(chat_id = ziweiid, text = "Input message below")
    return 0
    
def passtohuiting(update, context):
    chatid = update.message.chat_id
    chatmessage = update.message.text
    bot.send_message(chat_id = huitingid, text = chatmessage)
    bot.send_message(chat_id = chatid, text = "sent: "+ chatmessage)

def main():
    updater = Updater(
        TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    dp.add_handler(CommandHandler(["start","help"], start))
    dp.add_handler(CommandHandler("pingupat", pingupat))
    dp.add_handler(CommandHandler("pingu", pingu))
    dp.add_handler(CommandHandler("buttshake", buttshake))
    dp.add_handler(CommandHandler(["photo", "photos", "pics", "pic", "ourpics", "ourpic"], ourpics))
    dp.add_handler(CommandHandler(["ziweipics", "ziweipic", "ziweiphoto", "ziweiphotos"], ziweipics))
   
    send_to_huiting_handler = ConversationHandler(
        entry_points = [CommandHandler("sendtohuiting", sendtohuitingprompt)],
        states = {0: [MessageHandler(Filters.text, passtohuiting)]},
        fallbacks = [CommandHandler('help',start)])
    
    dp.add_handler(send_to_huiting_handler)

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