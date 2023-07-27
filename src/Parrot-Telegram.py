import logging
import json

import telegram.error

from utils import db, config, passwords

with open('../credentials.json') as f:
    tokens = json.load(f)
    committees_token = tokens["SailoreCommitteesBot"]
    parrot_token = tokens["SailoreParrotBot"]
    sailore_token = tokens["SailoreBXBot"]

with open('../data/Committees/committees.json') as f:
    committees = json.load(f)

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
from telegram import Update, Bot
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

class Committees_hub:
    def __init__(self):
        self.list = list(committees.keys())
        self.list.insert(0, '')
        self.committees_list = "\n -  ".join(self.list)
        [self.HOME, self.ADMIN, self.COMMITTEE, self.MESSAGE] = range(4)
        self.active_committee = ''

        self.committees_handler = ConversationHandler(
            entry_points=[MessageHandler(filters.TEXT, self.start)],
            states={
                self.HOME: [CommandHandler("admin", self.admin)],
                self.ADMIN: [MessageHandler(filters.TEXT, self.committee)],
                self.COMMITTEE: [MessageHandler(filters.TEXT, self.password)],
                self.MESSAGE: [MessageHandler(filters.TEXT, self.parrot)]
            },
            fallbacks=[CommandHandler("admin", self.admin),
                       MessageHandler(filters.TEXT, self.start)]
        )
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(chat_id=update.effective_user.id,
                                       text="This bot is for committees to manage their bot sections")
        await context.bot.send_message(chat_id=update.effective_user.id,
                                       text="To log into your committee use /admin")
        return self.HOME
    async def admin(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="To which committee do you want to log in?" + self.committees_list)
        return self.ADMIN

    async def committee(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        committee = update.message.text
        if committee in committees.keys():
            self.active_committee = committees[committee]
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text="What is the password?")
            return self.COMMITTEE
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text="That is not a valid committee")
            return self.ADMIN

    async def password(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        password = update.message.text

        if passwords.verify_password(db.get_pass_committee(self.active_committee),password):
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text="Logged in successfully")
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text="Which message do you want to send to your subscriptors?")
            db.record_logging(update.effective_user, self.active_committee)
            return self.MESSAGE
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text="Incorrect password")
            db.user_wrong_password(update.effective_user)
            return self.HOME

    async def parrot(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        message = update.message.text
        keys = db.subs_of_committee(self.active_committee)
        users_info = db.get_users_info(keys)
        parrot_bot = Bot(parrot_token)
        sailore_bot = Bot(sailore_token)
        counter = 0
        for user in users_info:
            try:
                await parrot_bot.send_message(chat_id=user['id'],
                                               text=f'Hello {user["name"]}, this is a communication from {self.active_committee}:')
                await parrot_bot.send_message(chat_id=user['id'], text=message)
            except telegram.error.BadRequest:
                counter += 1
                await sailore_bot.send_message(chat_id=user['id'],
                    text=f"""Hello {user['name']}, a communication from one of your subscriptions was just sent to you but you didn't receive it as you haven't signed in into t.me/SailoreParrotBot""")
        await context.bot.send_message(chat_id=update.effective_user.id,
                                       text="Successfully echoed your message")
        if counter > 0:
            await context.bot.send_message(chat_id=update.effective_user.id,
                                           text=f"We also notified {counter} of your users which didn't sign into @SailoreParrotBot")
        return self.HOME

def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(committees_token).build()
    committees_hub = Committees_hub()
    application.add_handler(committees_hub.committees_handler)

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()