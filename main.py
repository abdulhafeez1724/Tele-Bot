import telegram.ext
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")

def start(update, context):
    update.message.reply_text("hell form my Hafeez bot.")


def helps(update, context):
    update.message.reply_text(
        """
            Hi there what kind of help you want
            /start this command will start bot
            /content - we have different bot what you want
            /youtube
        """
    )

def youtube(update, context):
    update.message.reply_text(
        """
            you can check this link with  below 
            /link this command will start bot
  
            / 
        """
    )


def message_handler(update, context):
    update.message.reply_text(f" your message is {update.message.text}")

updater = telegram.ext.Updater(TOKEN, use_context= True)
dispatch = updater.dispatcher

dispatch.add_handler(telegram.ext.CommandHandler('start', start))
dispatch.add_handler(telegram.ext.CommandHandler('helps', helps))
dispatch.add_handler(telegram.ext.CommandHandler('youtube', youtube))

dispatch.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, message_handler))
dispatch.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, message_handler))


updater.start_polling()
updater.idle()

