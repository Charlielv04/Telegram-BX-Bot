import logging
import re
import time
import json
from typing import Dict
from Lore import members 

with open('credentials.json') as f:
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

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

INITIAL, LORE, TYPING_CHOICE = range(3)

reply_keyboard = [
    ["Age", "Favourite colour"],
    ["Number of siblings", "Something else..."],
    ["Done"],
]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)


def facts_to_str(user_data: Dict[str, str]) -> str:
    """Helper function for formatting the gathered user info."""
    facts = [f"{key} - {value}" for key, value in user_data.items()]
    return "\n".join(facts).join(["\n", "\n"])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Start the conversation and ask user for input."""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(1)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Ahoy Sailor, what can I help you with")
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(1)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="We can talk about those shiny gems, the mighty Sail'ore or the different committees a pirate can join")
    return INITIAL

async def gems(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Tell them a little bit about gems, in the future it will give more options but for that I'll have to ask Gaia and Adrien about IW"""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(1)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Oh me matey, gems are the most important currency in all of the seven seas")
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(1)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="They've been studied for centuries and they are central to Gemconomy")
    return INITIAL

async def lore(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Tell them a little bit about Sailore and allows them to learn about each of the members"""
    await context.bot.send_message(chat_id=update.effective_chat.id, text="The mighty Sail'ore you wanna learn about?")
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(1)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="This small but strong group of pirates once conquered the bachelor and, now, as they used to say they bring you party and crepes and fun")
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(1)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Do you want to learn about any of these pirates: Adrien, Eli, Giselle, Nic, Jeanne, Ryan, Akira, Ipop, Gaia or Angela")

    return LORE

def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(bot_token).build()

    # Add conversation handler with the states CHOOSING, TYPING_CHOICE and TYPING_REPLY
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            INITIAL: [
                MessageHandler(
                    filters.Regex(re.compile(r'gems', re.IGNORECASE)), gems
                ),
                MessageHandler(
                    filters.Regex(re.compile(r"l'?ore", re.IGNORECASE)), lore
                ),
            ],
            LORE: [
                MessageHandler(
                    filters.Regex(re.compile(r'adrien', re.IGNORECASE)), members.Adrien
                ),
                MessageHandler(
                    filters.Regex(re.compile(r'eli', re.IGNORECASE)), members.Eli
                ),
                MessageHandler(
                    filters.Regex(re.compile(r'giselle', re.IGNORECASE)), members.Giselle
                ),
                MessageHandler(
                    filters.Regex(re.compile(r'nic', re.IGNORECASE)), members.Nic
                ),
                MessageHandler(
                    filters.Regex(re.compile(r'jeanne', re.IGNORECASE)), members.Jeanne
                ),
                MessageHandler(
                    filters.Regex(re.compile(r'ryan', re.IGNORECASE)), members.Ryan
                ),
                MessageHandler(
                    filters.Regex(re.compile(r'akira', re.IGNORECASE)), members.Akira
                ),
                MessageHandler(
                    filters.Regex(re.compile(r'ipop', re.IGNORECASE)), members.Ipop
                ),
                MessageHandler(
                    filters.Regex(re.compile(r'gaia', re.IGNORECASE)), members.Gaia
                ),
                MessageHandler(
                    filters.Regex(re.compile(r'angela', re.IGNORECASE)), members.Angela
                ),

            ],
        },
        fallbacks=[MessageHandler(filters.TEXT, start)],
    )

    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()