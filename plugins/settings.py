import os
import importlib
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import config
from bot import Bot

@Bot.on_message(filters.command("settings") & filters.user(config.OWNER_ID))
async def settings_menu(client, message):
    protect_content_status = "✅" if config.PROTECT_CONTENT else "❌"
    buttons = [
        [InlineKeyboardButton(f"Protect Content {protect_content_status}", callback_data="toggle_protect_content")]
    ]
    await message.reply("Settings Menu:", reply_markup=InlineKeyboardMarkup(buttons))

@Bot.on_callback_query(filters.regex(r"toggle_protect_content"))
async def toggle_protect_content(client, callback_query):
    # Toggle the PROTECT_CONTENT value
    new_status = not config.PROTECT_CONTENT
    os.environ["PROTECT_CONTENT"] = "True" if new_status else "False"

    # Reload the config module to propagate changes
    importlib.reload(config)

    # Update the button text
    protect_content_status = "✅" if config.PROTECT_CONTENT else "❌"
    buttons = [
        [InlineKeyboardButton(f"Protect Content {protect_content_status}", callback_data="toggle_protect_content")]
    ]
    await callback_query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))