import time
from typing import Dict
import json
import re
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

reply_keyboard = [
    ["Yay", "Nay"],
]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

INITIAL, LORE, CONTINUE = range(3)

with open('../data/lore_descriptions.json', encoding='utf-8') as f:
    members_desc = json.load(f)

async def member(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """General Sailore member info function"""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(3)
    try:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=members_desc[update.message.text.capitalize()])
    except KeyError:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Oh me matey, I don't know that pirate")
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(0.5)
    await context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=markup,
                                   text="Do you want to learn about any other pirate?")
    return CONTINUE