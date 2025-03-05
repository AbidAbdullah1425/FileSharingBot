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
    buttons = [
        [
            InlineKeyboardButton(
                text="Enable Protect Content" if not config.PROTECT_CONTENT else "Disable Protect Content",
                callback_data="toggle_protect_content"
            )
        ],
        [
            InlineKeyboardButton(
                text="Reload Config",
                callback_data="reload_config"
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply("Settings Menu:", reply_markup=reply_markup)

@Bot.on_callback_query(filters.regex("toggle_protect_content") & filters.user(config.OWNER_ID))
async def toggle_protect_content(client, query):
    config.PROTECT_CONTENT = not config.PROTECT_CONTENT
    os.environ['PROTECT_CONTENT'] = str(config.PROTECT_CONTENT)
    reload_config()
    await query.message.edit_text(
        f"Protect Content is now {'enabled' if config.PROTECT_CONTENT else 'disabled'}.\n\nSettings Menu:",
        reply_markup=query.message.reply_markup
    )

@Bot.on_callback_query(filters.regex("reload_config") & filters.user(config.OWNER_ID))
async def reload_config_callback(client, query):
    reload_config()
    await query.message.edit_text(
        "Config reloaded.\n\nSettings Menu:",
        reply_markup=query.message.reply_markup
    )