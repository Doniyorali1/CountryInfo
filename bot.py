"""
Muallif lik huquqi Arslonbek Xushboqov (@LiderBoy) ga tegishli.

"""
import os
import pyrogram
import asyncio
import time
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent
from countryinfo import CountryInfo
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

client = Client(
    "Country Info Uzb Bot",
    bot_token = "1827287185:AAHSgM5GK7w-3rxdLJg9JySCAPQ1v_D5VDs",
    api_id = 4725624, #api_id
    api_hash = "ec25de708988860cd3db060aac2f2927" #api_hash
)

START_TEXT = """
Assalomu alaykum  {}, \nMen davlat haqidagi qiziqarli maʼlumotlarni qidiruvchi botman. \nMenga birorta davlat nomini ingliz tilida yuboring men sizga u haqidagi maʼlumotlarni yuboraman!
"""
HELP_TEXT = """
- Menga davlat nomini ingliz tilida yuboring.
- Men davlat nomini tekshiraman va u haqidagi maʼlumotlarni sizga yuboraman.
"""
ABOUT_TEXT = """
Ushbu bot maʼlumotlarni Wikipedia saytidan oladi.\nBot dasturchisi: Arslonbek Xushboqov (@LiderBoy)
"""
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Yordam ⚡', callback_data='help'),
        InlineKeyboardButton('Bot haqida❕', callback_data='about'),
        ],[
        InlineKeyboardButton('❌', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Bosh menu 🏠', callback_data='home'),
        ],[
        InlineKeyboardButton('❌', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Bosh menu 🏠', callback_data='home'),
        ],[
        InlineKeyboardButton('❌', callback_data='close')
        ]]
    )
ERROR_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Yordam ⚡', callback_data='help'),
        ],[
        InlineKeyboardButton('❌', callback_data='close')
        ]]
    )

@client.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            reply_markup=START_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            reply_markup=HELP_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.message.delete()

@client.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=START_BUTTONS
    )

@client.on_message(filters.private & filters.text)
async def countryinfo(bot, update):
    country = CountryInfo(update.text)
    info = f"""
Nomi : `{country.name()}`
Asl nomi : `{country.native_name()}`
Poytaxt : `{country.capital()}`
Aholisi : `{country.population()}`
Mintaqa : `{country.region()}`
Sub Mintaqa : `{country.subregion()}`
Asosiy domen nomi : `{country.tld()}`
Qoʻngʻiroq kodi: `{country.calling_codes()}`
Valyutasi : `{country.currencies()}`
Vaqt mintaqasi : `{country.timezones()}`

**Maʼlumotlar wikipedia.org saytidan olindi...**
"""
    country_name = country.name()
    country_name = country_name.replace(" ", "+")
    reply_markup=InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Wikipedia', url=f'{country.wiki()}'),
        ],[
        InlineKeyboardButton('❌', callback_data='close')
        ]]
    )
    try:
        await update.reply_text(
            text=info,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
    except Exception as error:
        print(error)
client.run()
