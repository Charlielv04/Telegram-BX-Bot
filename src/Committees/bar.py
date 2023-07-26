import re
import time
import gspread
from src.config import *

from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)


class Bar:
    def __init__(self):
        self.REPLY_KEYBOARD = [
            ["Yay", "Nay"],
        ]
        self.MARKUP = ReplyKeyboardMarkup(self.REPLY_KEYBOARD, one_time_keyboard=True)
        
        self.GC = gspread.service_account(ROOT + '/service_account.json')
        self.SH = self.GC.open("BX-telegram")
    
        self.BOARD_MEMBERS = "\n".join(["Prez: Carlos", "VPrez: Maxime", "Stock: Gabin", "Comms: Alix", "Events: Anahí", "Sked: Johanna", "Bartenders: Arturo, Antoine"])
        self.EXIT, self.HOME, self.SUB = range(3)

        self.bar_handler = ConversationHandler(
            entry_points=[CommandHandler("bar", self.bar_intro)],
            states={
                self.HOME: [
                    MessageHandler(
                        filters.Regex(re.compile(r'board', re.IGNORECASE)), self.bar_board
                    ),
                    CommandHandler("sub", self.sub),
                    CommandHandler("exit", exit)
                ],
            },
            fallbacks=[MessageHandler(filters.TEXT, self.bar_intro)],
            map_to_parent={
                # Connection to the parent handler, note that its written EXIT: EXIT where both of these are equal to 0, that's why it leads to INITIAL which is also equal to 0
                self.EXIT: self.EXIT
            }
        )

    async def bar_intro(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
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
        return self.HOME
    
    async def bar_board(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Introduces the bar board"""
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
        time.sleep(1.2)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="The .9 bar is excellent we have lots of motivated people here")
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
        time.sleep(1.2)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="The members of the board are the following:\n" + BOARD_MEMBERS)
        return self.HOME
    
    async def exit(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Exit of the committee section"""
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
        time.sleep(1.2)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="See you again whenever you want to explore this great committee")
    
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
        time.sleep(2)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="After that, what do you want to talk about, we can talk about those shiny gems, the mighty Sail'ore or the different committees a pirate can join")
        return self.EXIT
    
    async def sub(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Checks if the user is subscribed and allows it to toogle it"""
        sheet = SH.worksheet("Committee subscriptions")
        ids = sheet.col_values(sheet.find(".9 Bar").col + 1)[1:]
        if update.message.chat.id in ids:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="It seems like you already subscribed to this committee") 
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="It seems like you aren't subscribed to this committee")
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Do you wanna subscribe to it?", reply_markup=MARKUP)
            await self.subscribe(update.message.chat.first_name, update.message.chat.id, ".9 Bar")
    
    async def checksub(self, id, committee_name):
        sheet = self.SH.worksheet("Committee subscriptions")
        ids = sheet.col_values(sheet.find(committee_name).col + 1)[1:] 
        return id in ids
    
    async def subscribe(self, name, id, committee_name):
        sheet = self.SH.worksheet("Committee subscriptions")
        column = sheet.find(committee_name).col
        print(sheet.find(committee_name).address)
        names = sheet.col_values(column)[1:]