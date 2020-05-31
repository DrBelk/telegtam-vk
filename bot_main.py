from telegram.ext import Updater
from telegram.ext import CommandHandler
from bot_privacy import API_TOKEN

updater = Updater(token=API_TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def set_vk_user_handler(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Setting up the main user, please type VK login")

start_handler = CommandHandler('start', start)
set_vk_user_handler = CommandHandler('set_vk_user', set_vk_user_handler)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(set_vk_user_handler)


updater.start_polling()

