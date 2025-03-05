import os
import importlib
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import config
from bot import Bot

###-----------------------------###
def reload_config():
    importlib.reload(config)
    

###-----------------------------###
@Bot.on_message(filters.command("settings") & filters.user(config.OWNER_ID))
async def settings_menu(client, message):
    