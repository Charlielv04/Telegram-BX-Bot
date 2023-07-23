import logging
import re
import time
import json
from typing import Dict
from Lore import members 
from Committees import bar, physiX

with open('../credentials.json') as f:
    bot_token = json.load(f)["bot_token"]

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
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)
aa = "Adrien"
# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

INITIAL, LORE, CONTINUE, COMMITTEES = range(4)

committees_list = "\n -  ".join(["",".9 bar🍻🍻 (/bar)", "PhysiX⚛️⚛️ (/Physix)", "ClimbX (/ClimbX)"])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Start the conversation and ask user for input."""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(0.6)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Ahoy Sailor, what can I help you with?")
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(1.2)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="We can talk about those shiny gems, the mighty Sail'ore or the different committees a pirate can join")
    return INITIAL

async def gems(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Tell them a little bit about gems, in the future it will give more options but for that I'll have to ask Gaia and Adrien about IW"""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(0.8)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Oh me matey, gems are the most important currency in all of the seven seas")
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(1.1)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="They've been studied for centuries and they are central to Gemconomy. However right now they are nowhere to be seen.")
    return INITIAL

async def lore(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Tell them a little bit about Sailore and allows them to learn about each of the members"""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(0.5)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="The mighty Sail'ore you wanna learn about?")
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(1)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="This small but strong group of pirates once conquered the bachelor and, now, as they used to say they bring you party and crepes and fun")
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(0.8)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="If you wish to learn about any of these pirates just tell me their name: Adrien, Eli, Giselle, Nic, Jeanne, Ryan, Akira, Ipop, Gaia or Angela")
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
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(0.8)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Oh me matey I didn't understand what you meant, but I know lots of other stories")
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(1.2)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="We can talk about those shiny gems, the mighty Sail'ore or the different committees a pirate can join")
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


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(bot_token).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
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
                physiX.physix_handler
            ],
        },
        fallbacks=[MessageHandler(filters.TEXT, predetermined)],
    )
    
    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()