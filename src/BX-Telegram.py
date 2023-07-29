import logging
import re
import time
import json
import math
import Lore
import Committees
from utils import db, config
import utils
import asyncio

with open('../credentials.json') as f:
    bot_token = json.load(f)["SailoreBXBot"]

with open('../data/Initial.json', encoding='utf-8') as f:
    texts = json.load(f)

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

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

INITIAL, LORE, CONTINUE, COMMITTEES = range(4)

committees_list = "\n -  ".join(["",".9 bar🍻🍻 (/bar)", "PhysiX⚛️⚛️ (/Physix)", "ClimbX (/ClimbX)"])

def message_wait(message):
    return math.log(len(message), 10)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Start the conversation and ask user for input."""
    for message in texts["start"]:
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
        time.sleep(message_wait(message))
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    db.add_to_db(update.effective_user)
    return INITIAL

async def gems(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Tell them a little bit about gems, in the future it will give more options but for that I'll have to ask Gaia and Adrien about IW"""
    for message in texts["gems"]:
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
        time.sleep(message_wait(message))
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    await context.bot.send_message(chat_id=5454590173, text="Hello Gianluca I'm seeing you")
    return INITIAL

async def lore(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Tell them a little bit about Sailore and allows them to learn about each of the members"""
    for message in texts["lore"]:
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
        time.sleep(message_wait(message))
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    return LORE

async def more(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Ask about what other pirate do they wanna learn about"""
    time.sleep(0.8)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Which other pirate do you want to learn about me matey?")
    return LORE

async def nomore(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Same as start but a bit different"""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(0.6)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="What other stories can I tell you?")
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(1.2)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="We can talk about those shiny gems, the mighty Sail'ore or the different committees a pirate can join")
    return INITIAL

async def predetermined(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Predetermined message when something is not understood"""
    for message in texts["predetermined"]:
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
        time.sleep(message_wait(message))
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    return INITIAL

async def committees(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Tell them about the different committees"""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(1.2)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Committees are the central part of our piratey studen life, there is lots of them and if you don't find the one you want, you can even create a new one")
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(0.9)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Here is the full list of committees:" + committees_list)
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(1.1)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="To enter a committee section just press the command next to its name")
    return COMMITTEES


async def main() -> None:
    """Run the bot."""
    asyncio.create_task(utils.scan(3600))
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(bot_token).build()
    
    bar = Committees.Bar()
    physix = Committees.Physix()
    members = Lore.Members()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start), MessageHandler(filters.TEXT, start)],
        states={
            INITIAL: [ 
                #Initial state of the bot in which it can be asked about gems, the lore and committees
                MessageHandler(
                    filters.Regex(re.compile(r'gems', re.IGNORECASE)), gems
                ),
                MessageHandler(
                    filters.Regex(re.compile(r"l'?ore", re.IGNORECASE)), lore
                ),
                MessageHandler(
                    filters.Regex(re.compile(r"com?mit?te?es", re.IGNORECASE)), committees #added the question marks cuz people tend to mispell this word
                ),
            ],
            LORE: [
                #State of the bot in which it can be asked about the different sailore members
                MessageHandler(filters.TEXT, members.member)
            ],
            CONTINUE: [
                #State of the bot in which it is asked if it wants to continue asking about sailore members
                MessageHandler(
                    filters.Regex(re.compile(r'yay', re.IGNORECASE)), more
                ),
                MessageHandler(
                    filters.Regex(re.compile(r'nay', re.IGNORECASE)), nomore
                )
            ],
            COMMITTEES:  [
                #State of the bot in which the committees children handlers can be accessed
                bar.bar_handler,
                physix.physix_handler
            ],
        },
        fallbacks=[MessageHandler(filters.TEXT, predetermined)],
    )
    
    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
