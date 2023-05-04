from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello, World!')

def echo(update: Update, context: CallbackContext):
    text = update.message.text
    update.message.reply_text(text)

