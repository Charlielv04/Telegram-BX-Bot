import re
import time
from typing import Dict

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

async def physix(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Intro for physix"""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(1.2)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the PhysiX section of the Telegram Bot")
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(1.2)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="In here you can learn about our board, get the link to join our groupchat, find out about our next events and even subscribe to our notifications from this bot")

physix_handler = ConversationHandler(
        entry_points = [CommandHandler("PhysiX", physix)],
        states={
            1: [],
        },
        fallbacks=[MessageHandler(filters.TEXT, physix)]
    )

