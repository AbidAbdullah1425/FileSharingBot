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
        [InlineKeyboardButton(f"Protect Content {protect_content_status}", callback_data="set_protect_content")]
    ]
    await message.reply("Settings Menu:", reply_markup=InlineKeyboardMarkup(buttons))

@Bot.on_callback_query(filters.regex(r"set_protect_content"))
async def set_protect_content(client, callback_query):
    # Toggle the value
    new_status = not config.PROTECT_CONTENT

    # Update environment variable
    os.environ["PROTECT_CONTENT"] = "True" if new_status else "False"

    # Reload config to apply the new environment variable
    importlib.reload(config)

    # Acknowledge button click
    await callback_query.answer(f"Protect Content set to {'Enabled' if new_status else 'Disabled'}!", show_alert=False)

    # Update button
    protect_content_status = "✅" if new_status else "❌"
    buttons = [
        [InlineKeyboardButton(f"Protect Content {protect_content_status}", callback_data="set_protect_content")]
    ]
    await callback_query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
