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

reply_keyboard = [
    ["Yay", "Nay"],
]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

INITIAL, LORE, CONTINUE = range(3)

async def Adrien(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Tell them a little bit about this Sailore member"""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(3)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="""Ah, Adrien, the General Secretary of Sail'Ore, or simply the boss. With his chiseled abs and charming French accent, this croissant-eating heartthrob could charm the pants off of anyone - but honestly, he'd probably rather charm a bucket of KFC chicken. Yes, Adrien's been known to put away more fried chicken than a small village. His playful and humorous personality adds to his appeal, although sometimes his jokes can be a bit risqué, especially when he's engaging in playful same-sex behavior with Gaia. Despite his alluring charms, Adrien is more than just a pretty face. He's an invaluable asset to our team, bringing a unique perspective and a strong work ethic to the table. His unparalleled dedication and exceptional ability to execute projects from creative directing to logistics make him the ideal general secretary for Sail'Ore.""")
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(0.5)
    await context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=markup, text="Do you want to learn about any other pirate?")
    return CONTINUE

async def Eli(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Tell them a little bit about this Sailore member"""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(3)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Meet Elisabeth, the woman in charge of the Bachelor Committees and Binets relations. This wine-loving enthusiast has a personality that's as bold as the cabernet sauvignon she drinks. With her outgoing and particularly social personality and collaborative working skills, she does a great job overlooking our diverse body of Bachelor committees. Elizabeth's organizational skills are second to none, and she has a particular talent for bringing people together for more than just drinking wine. She's the ideal bridge between us and the engineers and is a great asset to the enhancement and optimization of your stay on campus; she's an exceptional listener and you can be certain that - with her in charge - your project or committee-related ideas will be swiftly brought to everyone's attention and put in place.")
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(0.5)
    await context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=markup, text="Do you want to learn about any other pirate?")
    return CONTINUE

async def Giselle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Tell them a little bit about this Sailore member"""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(3)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Introducing big Gigi. No, that’s a lie: she’s in fact tiny. The tiniest of us all. But don't let her size fool you: she may be small, but her screams when we mess up our dance routines could rival the loudest foghorns at sea. And speaking of dance routines, have you seen Giselle in action? It's like watching a ballerina on steroids. She moves with such grace and precision, it's no wonder she's a star cheerleader. But Giselle isn't just about dancing and screaming. She's also the mastermind behind all our events, using her organizational skills to make sure everything runs like a well-oiled machine. So, if you want someone who can kick butt and plan a killer event, just call Giselle!")
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(0.5)
    await context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=markup, text="Do you want to learn about any other pirate?")
    return CONTINUE

async def Nic(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Tell them a little bit about this Sailore member"""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(3)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="It is an honor to introduce our very own British royalty and chess master; Nicolas, also known as (or even exclusively known as) Nic, in charge of Sail'Ore's Internal Relations. It is to no one's surprise that pepper is as spicy as the English man's food gets. His speaking skills are unparalleled and enough to swiftly put us all in action. But don't let his charisma fool you, this man is all business. As the head of internal relations, he's the glue that holds our team together. Nic does not back down from a challenge; be it Shanya at a chess competition or Nando's spicy sauce, you can count on him to get the job done. His specialty is bland chicken.")
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(0.5)
    await context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=markup, text="Do you want to learn about any other pirate?")
    return CONTINUE

async def Jeanne(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Tell them a little bit about this Sailore member"""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(3)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Billie Jeanne is not my lover. But she’s a girl you can count on for professional relations! Riding a cool and sleek BMW to campus, she’s already your regular businesswoman, ready to close deals and make connections. Actually, scratch that: she’s downright a bona fide boss. She's a woman with a plan,and the drive to make it happen, and she's a crucial element of our power as a l'Ore. But her game goes far beyond just phone calls; she's got game both on and off the court! Yes, that's right, Jeanne can shoot those 3 pointers like nobody's business. So, if you're looking for someone who can score both in the boardroom and on the basketball court, look no further than Jeanne. She's a Sail'Ore MVP!")
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(0.5)
    await context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=markup, text="Do you want to learn about any other pirate?")
    return CONTINUE

async def Ryan(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Tell them a little bit about this Sailore member"""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(3)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="ChatGPT could not interpret “Infrastructure role”. I mean, I can’t blame it: who knows what that role means? Not Ryan, that’s for sure. So here I am writing his description, and, as his good friend, I will take it upon myself to introduce this unit of a man to you all. Certified lover boy hailing from Lebanon, he knows better than anyone else how to make bodies swing and sway to his hypnotizing beats. When he’s not making other bodies move, he’s swerving his own left and right with a basketball around even the tallest defense. All jokes aside, I’m pretty sure he takes care of all batiment and foyer related issues. And trust me, this man is more than qualified to keep this building sturdier than Bronx drill.")
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(0.5)
    await context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=markup, text="Do you want to learn about any other pirate?")
    return CONTINUE

async def Akira(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Tell them a little bit about this Sailore member"""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(3)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="His parents call him Akira, but it is nothing less than a shame not to call him by his well-earned title; SushiChamp150. That’s right, this is the absolute legend that sacrificed his abdomen for a mention on the all promo chat. Nonetheless, this colossal representation of athleticism itself is in charge of Sail’Ore sports activities! You may or may not know him from the various sports team he’s already involved in. SushiChamp is also the embodiment of diversity, bearing Welsh, Japanese, and Argentinian roots in him! (Yeah he’s lasian) He’s also my partner in bearing the burden of writing these introductions; you may have deduced that from the strong fluctuation in description quality. Nevertheless, there is no doubt that Akira is best-equipped for structuring and putting in place exceptionally engaging sports events and activities.")
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(0.5)
    await context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=markup, text="Do you want to learn about any other pirate?")
    return CONTINUE

async def Ipop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Tell them a little bit about this Sailore member"""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(3)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="You can call her Ioana, Ipop, Popi, Popipuscu, or anytime ;). Sail’ore’s communications representative is up 24/7 to deal with any and all complaints! Not only a mighty mathematical menace, she’s a diligent communicator, and you can count on her to never ghost you. Fear of missing out? Fear no more! With Ipop, you’ll always be part of the cool kids, and know exactly when and where our best events are.")
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(0.5)
    await context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=markup, text="Do you want to learn about any other pirate?")
    return CONTINUE

async def Gaia(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Tell them a little bit about this Sailore member"""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(3)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sailore’s very own resident minor: Gaia. At just 17 years old, this young blood brings a new and fresh mindset to the team, with innovative ideas and ambitious plans. But even fresher than his mindset is his drip: this boy rocks out a pair of shorts and sweater, even in the coldest conditions known to humanity. On top of that, his intelligence is unmatched, as we can deduce from his megamind-sized brain that even his sweater’s hood cannot hide. With all these qualities, who else could be a better fit for integration? He is sure to level with the BX26s and make sure everyone feels welcome and included. This kid may be the baby of the campaign, but he's got the brains and heart to make a real difference.")
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(0.5)
    await context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=markup, text="Do you want to learn about any other pirate?")
    return CONTINUE

async def Angela(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Tell them a little bit about this Sailore member"""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(3)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Meet Angela, Sail'Ore's very own treasurer from the Canary Islands! This sharp-minded island girl brings a strong, and exceptionally determined personality to the team and, with her fierce and effective approach when it comes to achieving the set-out goals, she is a force to be reckoned with. Some people might be intimidated by Angela's no-nonsense attitude, but let's be real - that's the type of person we want in charge of our finances. And if someone tries to mess with her, then let's just say they'll be dealing with one pissed-off, fiery Latina. From sourcing to spending, Angela keeps everything in check and ensures the success and feasibility of our events.")
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    time.sleep(0.5)
    await context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=markup, text="Do you want to learn about any other pirate?")
    return CONTINUE
