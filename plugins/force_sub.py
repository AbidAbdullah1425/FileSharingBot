from pyrogram import Client, filters
from pyrogram.types import Message
from config import DB_NAME, DB_URL
import importlib
import os
import config
from bot import Bot
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient(DB_URL)
db = client[DB_NAME]
collection = db['force_sub_channels']

def update_force_sub_channel(channel_number, new_value):
    os.environ[f"FORCE_SUB_CHANNEL{channel_number}"] = str(new_value)
    reload_config()
    collection.update_one(
        {'_id': f"FORCE_SUB_CHANNEL{channel_number}"},
        {'$set': {'value': new_value}},
        upsert=True
    )

def reload_config():
    importlib.reload(config)

@Bot.on_message(filters.command("fsub1") & filters.user(config.OWNER_ID))
async def set_force_sub_channel1(client, message: Message):
    try:
        new_value = int(message.command[1])
    except (IndexError, ValueError):
        await message.reply_text("Please provide a valid new value for FORCE_SUB_CHANNEL1.")
        return

    update_force_sub_channel(1, new_value)
    await message.reply_text(f"FORCE_SUB_CHANNEL1 updated to {new_value}")

@Bot.on_message(filters.command("fsub2") & filters.user(config.OWNER_ID))
async def set_force_sub_channel2(client, message: Message):
    try:
        new_value = int(message.command[1])
    except (IndexError, ValueError):
        await message.reply_text("Please provide a valid new value for FORCE_SUB_CHANNEL2.")
        return

    update_force_sub_channel(2, new_value)
    await message.reply_text(f"FORCE_SUB_CHANNEL2 updated to {new_value}")

@Bot.on_message(filters.command("fsub3") & filters.user(config.OWNER_ID))
async def set_force_sub_channel3(client, message: Message):
    try:
        new_value = int(message.command[1])
    except (IndexError, ValueError):
        await message.reply_text("Please provide a valid new value for FORCE_SUB_CHANNEL3.")
        return

    update_force_sub_channel(3, new_value)
    await message.reply_text(f"FORCE_SUB_CHANNEL3 updated to {new_value}")

@Bot.on_message(filters.command("fsub4") & filters.user(config.OWNER_ID))
async def set_force_sub_channel4(client, message: Message):
    try:
        new_value = int(message.command[1])
    except (IndexError, ValueError):
        await message.reply_text("Please provide a valid new value for FORCE_SUB_CHANNEL4.")
        return

    update_force_sub_channel(4, new_value)
    await message.reply_text(f"FORCE_SUB_CHANNEL4 updated to {new_value}")

@Bot.on_message(filters.command("show_fsubs") & filters.user(config.OWNER_ID))
async def show_fsubs(client, message: Message):
    importlib.reload(config)
    fsub_values = (
        f"FORCE_SUB_CHANNEL1: {config.FORCE_SUB_CHANNEL1}\n"
        f"FORCE_SUB_CHANNEL2: {config.FORCE_SUB_CHANNEL2}\n"
        f"FORCE_SUB_CHANNEL3: {config.FORCE_SUB_CHANNEL3}\n"
        f"FORCE_SUB_CHANNEL4: {config.FORCE_SUB_CHANNEL4}"
    )
    await message.reply_text(fsub_values)