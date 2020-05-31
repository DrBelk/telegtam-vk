from telegram.ext import Updater
from telegram.ext import CommandHandler
from error_codes import *
from vk_handler import vk_handler

try:
    from bot_privacy import API_TOKEN
except:
    print ('got real variables')
    from bot_privacy_real import API_TOKEN
    

class telegram_bot:
    # Telegram bot's functions
    def start(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="I'm a bot, please talk to me!")

    def set_vk_user_handler(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                 text="Setting up the main user, please type VK login")

    def start(self):
        updater = Updater(token=API_TOKEN, use_context=True)
        dispatcher = updater.dispatcher

        start_handler = CommandHandler('start', self.start)
        dispatcher.add_handler(start_handler)

        set_vk_user_handler = CommandHandler('set_vk_user', self.set_vk_user_handler)
        dispatcher.add_handler(set_vk_user_handler)

        updater.start_polling()
        
        print('Bot is working')


bot = telegram_bot()
bot.start()
                 
