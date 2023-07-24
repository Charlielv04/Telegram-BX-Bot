import re
import time
import gspread

from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

REPLY_KEYBOARD = [
    ["Yay", "Nay"],
]
MARKUP = ReplyKeyboardMarkup(REPLY_KEYBOARD, one_time_keyboard=True)


BOARD_MEMBERS = "\n".join(["Prez: Carlos", "VPrez: Maxime", "Stock: Gabin", "Comms: Alix", "Events: Anahí", "Sked: Johanna", "Bartenders: Arturo, Antoine"])
async def bar_intro(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Intro for the bar"""
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
    await context.bot.send_message(chat_id=update.effective_chat.id, text="The members of the board are the following:\n" + BOARD_MEMBERS)
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

async def sub(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Checks if the user is subscribed and allows it to toogle it"""
    sheet = SH.worksheet("Committee subscriptions")
    ids = sheet.col_values(sheet.find(".9 Bar").col + 1)[1:]
    if update.message.chat.id in ids:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="It seems like you already subscribed to this committee") 
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="It seems like you aren't subscribed to this committee")
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Do you wanna subscribe to it?", reply_markup=MARKUP)
        await subscribe(update.message.chat.first_name, update.message.chat.id, ".9 Bar")

async def subscribe(name, id, committee_name):


EXIT, HOME, SUB = range(3)

bar_handler = ConversationHandler(
    entry_points=[CommandHandler("bar", bar_intro)],
    states={
        HOME: [
            MessageHandler(
                filters.Regex(re.compile(r'board', re.IGNORECASE)), bar_board
            ),
            CommandHandler("sub", sub),
            CommandHandler("exit", exit)
        ],
    },
    fallbacks=[MessageHandler(filters.TEXT, bar_intro)],
    map_to_parent={
        #Connection to the parent handler, note that its written EXIT: EXIT where both of these are equal to 0, that's why it leads to INITIAL which is also equal to 0
        EXIT: EXIT
    }
)

