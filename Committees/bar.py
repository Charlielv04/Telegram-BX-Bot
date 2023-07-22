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
board_members = "\n".join(["Prez: Carlos", "VPrez: Maxime", "Stock: Gabin", "Comms: Alix", "Events: Anahí", "Sked: Johanna", "Bartenders: Arturo, Antoine"])
async def bar_intro(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Intro for physix"""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(1.2)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the .9bar section of the Telegram Bot")
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(1.2)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="In here you can learn about our board, get the link to join our groupchat, find out about our next events and even subscribe to our notifications from this bot")
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(1.2)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="To exit this section of the bot just use the command /exit")
    return HOME

async def bar_board(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Introduces the bar board"""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(1.2)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="The .9 bar is excellent we have lots of motivated people here")
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(1.2)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="The members of the board are the following:\n" + board_members)
    return HOME

async def exit(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Exit of the committee section"""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(1.2)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="See you again whenever you want to explore this great committee")
    
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(2)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="After that, what do you want to talk about, we can talk about those shiny gems, the mighty Sail'ore or the different committees a pirate can join")
    
    return EXIT

EXIT, HOME, SUB = range(3)

bar_handler = ConversationHandler(
    entry_points = [CommandHandler("bar", bar_intro)],
    states = {
        HOME: [
            MessageHandler(
                filters.Regex(re.compile(r'board', re.IGNORECASE)), bar_board
            ),
            CommandHandler("exit", exit)
        ],
    },
    fallbacks = [MessageHandler(filters.TEXT, bar_intro)],
    map_to_parent={
        EXIT: EXIT
    }
)

