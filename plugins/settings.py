import os
import importlib
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import config
from bot import Bot

@Bot.on_message(filters.command("settings") & filters.user(config.OWNER_ID))
async def settings_menu(client, message):
    protect_content_status = "✅" if os.getenv("PROTECT_CONTENT") == "True" else "❌"
    buttons = [
        [InlineKeyboardButton(f"Protect Content {protect_content_status}", callback_data="toggle_protect_content")]
    ]
    await message.reply("Settings Menu:", reply_markup=InlineKeyboardMarkup(buttons))

@Bot.on_callback_query(filters.regex(r"toggle_protect_content"))
async def toggle_protect_content(client, callback_query):
    # Toggle the PROTECT_CONTENT value
    current_status = os.getenv("PROTECT_CONTENT") == "True"
    new_status = not current_status
    os.environ["PROTECT_CONTENT"] = "True" if new_status else "False"

    # Reload the config module to propagate changes
    importlib.reload(config)

    # Update the button text directly
    protect_content_status = "✅" if new_status else "❌"
    buttons = [
        [InlineKeyboardButton(f"Protect Content {protect_content_status}", callback_data="toggle_protect_content")]
    ]
    await callback_query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))