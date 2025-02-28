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
    config.PROTECT_CONTENT = new_status

    # Update the config.py file
    with open("config.py", "r") as file:
        lines = file.readlines()
    with open("config.py", "w") as file:
        for line in lines:
            if line.strip().startswith("PROTECT_CONTENT"):
                file.write(f"PROTECT_CONTENT = {new_status}\n")
            else:
                file.write(line)

    # Reload the config module to propagate changes
    importlib.reload(config)

    # Update the button text
    protect_content_status = "✅" if config.PROTECT_CONTENT else "❌"
    buttons = [
        [InlineKeyboardButton(f"Protect Content {protect_content_status}", callback_data="toggle_protect_content")]
    ]
    await callback_query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    await callback_query.answer("Protect Content status toggled.")