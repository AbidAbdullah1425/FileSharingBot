from pyrogram import Client, filters
from pyrogram.types import Message
import importlib
import config
from bot import Bot

@Client.on_message(filters.command("fsub1") & filters.user(config.OWNER_ID))
async def set_force_sub_channel1(client, message: Message):
    await message.reply_text("Send the new value for FORCE_SUB_CHANNEL1")

@Client.on_message(filters.text & filters.reply & filters.user(config.OWNER_ID))
async def receive_new_force_sub_channel1(client, message: Message):
    if message.reply_to_message and message.reply_to_message.text == "Send the new value for FORCE_SUB_CHANNEL1":
        new_value = message.text.strip()
        config.FORCE_SUB_CHANNEL1 = int(new_value)
        reload_config()
        await message.reply_text(f"FORCE_SUB_CHANNEL1 updated to {new_value}")

def reload_config():
    importlib.reload(config)


