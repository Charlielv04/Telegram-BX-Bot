import logging
import re
import time
import json
import math
import Lore
import Committees
from utils import db

with open('../credentials.json') as f:
    bot_token = json.load(f)["SailoreParrotBot"]

from telegram import __version__ as TG_VER
try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

HOME, ADMIN, COMMITTEE, MESSAGE = range(4)

committees_list = "\n -  ".join(["",".9 bar🍻🍻 (/bar)", "PhysiX⚛️⚛️ (/Physix)", "ClimbX (/ClimbX)"])
async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_user.id)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="To which committee do you want to log in?")
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=committees_list)
    return ADMIN

async def bar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="What is the password?")
    return COMMITTEE

async def password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    password = update.message.text
    if password == '1234':
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Logged in succesfully")
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Which message do you want to send to your subscriptors?")
    return MESSAGE

async def parrot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text
    keys = db.subs_of_committee(".9 Bar")
    print(keys)
    ids = []
    for key in keys:
        ids.append(key.strip("user:"))
    for id in ids:
        await context.bot.send_message(chat_id=id, text=message)
    return HOME

def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(bot_token).build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("admin", admin)],
        states={
            HOME: [],
            ADMIN:[CommandHandler('bar', bar)],
            COMMITTEE:[MessageHandler(filters.TEXT, password)],
            MESSAGE:[MessageHandler(filters.TEXT, parrot)]
        },
        fallbacks=[]
    )
    application.add_handler(conv_handler)

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()