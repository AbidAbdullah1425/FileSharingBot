from pyrogram import Client, filters
from pyrogram.types import Message
import importlib
import config
from bot import Bot

@Bot.on_message(filters.command("fsub1") & filters.user(config.OWNER_ID))
async def set_force_sub_channel1(client, message: Message):
    await message.reply_text("Send the new value for FORCE_SUB_CHANNEL1")

@Bot.on_message(filters.text & filters.reply & filters.user(config.OWNER_ID))
async def receive_new_force_sub_channel1(client, message: Message):
    if message.reply_to_message and message.reply_to_message.text == "Send the new value for FORCE_SUB_CHANNEL1":
        new_value = message.text.strip()
        config.FORCE_SUB_CHANNEL1 = int(new_value)
        reload_config()
        await message.reply_text(f"FORCE_SUB_CHANNEL1 updated to {new_value}")

def reload_config():
    importlib.reload(config)






@Bot.on_message(filters.command("show_fsubs") & filters.user(config.OWNER_ID))
async def show_fsubs(client, message: Message):
    # Reload the config to ensure the latest values
    importlib.reload(config)
    
    # Fetch and display the FORCE_SUB_CHANNEL values
    fsub_values = (
        f"FORCE_SUB_CHANNEL1: {config.FORCE_SUB_CHANNEL1}\n"
        f"FORCE_SUB_CHANNEL2: {config.FORCE_SUB_CHANNEL2}\n"
        f"FORCE_SUB_CHANNEL3: {config.FORCE_SUB_CHANNEL3}\n"
        f"FORCE_SUB_CHANNEL4: {config.FORCE_SUB_CHANNEL4}"
    )
    
    await message.reply_text(fsub_values)


