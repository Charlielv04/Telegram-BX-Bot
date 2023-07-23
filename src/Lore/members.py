import time
from typing import Dict
import json
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

with open('../data/lore_descriptions.json') as f:
    members_desc = json.load(f)

async def member(update: Update, context: ContextTypes.DEFAULT_TYPE, message) -> int:
    """General Sailore member info function"""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(3)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(0.5)
    await context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=markup,
                                   text="Do you want to learn about any other pirate?")
    return CONTINUE


async def test_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """member wrapper for specific lore member test_member """
    return member(update, context, "test_member message")


async def Adrien(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Tell them a little bit about this Sailore member"""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(3)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=members_desc["Adrien"])
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(0.5)
    await context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=markup, text="Do you want to learn about any other pirate?")
    return CONTINUE

async def Eli(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Tell them a little bit about this Sailore member"""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(3)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=members_desc["Eli"])
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(0.5)
    await context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=markup, text="Do you want to learn about any other pirate?")
    return CONTINUE

async def Giselle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Tell them a little bit about this Sailore member"""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(3)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=members_desc["Giselle"])
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(0.5)
    await context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=markup, text="Do you want to learn about any other pirate?")
    return CONTINUE

async def Nic(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Tell them a little bit about this Sailore member"""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(3)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=members_desc["Nic"])
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(0.5)
    await context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=markup, text="Do you want to learn about any other pirate?")
    return CONTINUE

async def Jeanne(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Tell them a little bit about this Sailore member"""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(3)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=members_desc["Jeanne"])
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(0.5)
    await context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=markup, text="Do you want to learn about any other pirate?")
    return CONTINUE

async def Ryan(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Tell them a little bit about this Sailore member"""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(3)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=members_desc["Ryan"])
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(0.5)
    await context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=markup, text="Do you want to learn about any other pirate?")
    return CONTINUE

async def Akira(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Tell them a little bit about this Sailore member"""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(3)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=members_desc["Akira"])
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(0.5)
    await context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=markup, text="Do you want to learn about any other pirate?")
    return CONTINUE

async def Ipop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Tell them a little bit about this Sailore member"""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(3)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=members_desc["Ipop"])
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(0.5)
    await context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=markup, text="Do you want to learn about any other pirate?")
    return CONTINUE

async def Gaia(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Tell them a little bit about this Sailore member"""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(3)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=members_desc["Gaia"])
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(0.5)
    await context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=markup, text="Do you want to learn about any other pirate?")
    return CONTINUE

async def Angela(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Tell them a little bit about this Sailore member"""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(3)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=members_desc["Angela"])
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(0.5)
    await context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=markup, text="Do you want to learn about any other pirate?")
    return CONTINUE
