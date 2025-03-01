import os
import importlib
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import config
from bot import Bot

# Dictionary to store temporary values during runtime (avoids delays)
temp_settings = {"PROTECT_CONTENT": config.PROTECT_CONTENT}

@Bot.on_message(filters.command("settings") & filters.user(config.OWNER_ID))
async def settings_menu(client, message):
    protect_content_status = "✅" if temp_settings["PROTECT_CONTENT"] else "❌"
    buttons = [
        [InlineKeyboardButton(f"Protect Content {protect_content_status}", callback_data="toggle_protect_content")]
    ]
    await message.reply("Settings Menu:", reply_markup=InlineKeyboardMarkup(buttons))

@Bot.on_callback_query(filters.regex(r"toggle_protect_content"))
async def toggle_protect_content(client, callback_query):
    # Toggle the value in the temporary dictionary
    temp_settings["PROTECT_CONTENT"] = not temp_settings["PROTECT_CONTENT"]

    # Update the environment variable
    os.environ["PROTECT_CONTENT"] = "True" if temp_settings["PROTECT_CONTENT"] else "False"

    # Reload config to reflect changes
    config.PROTECT_CONTENT = temp_settings["PROTECT_CONTENT"]

    # Ensure the bot processes the callback properly
    await callback_query.answer("Protect Content updated!", show_alert=False)

    # Update button
    protect_content_status = "✅" if temp_settings["PROTECT_CONTENT"] else "❌"
    buttons = [
        [InlineKeyboardButton(f"Protect Content {protect_content_status}", callback_data="toggle_protect_content")]
    ]
    await callback_query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
