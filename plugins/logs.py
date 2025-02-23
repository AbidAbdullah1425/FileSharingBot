import os
from bot import Bot
from pyrogram import Client, filters
from pyrogram.types import Message

@Bot.on_message(filters.private & filters.command('logs') & filters.user(ADMINS))
async def send_logs(client: Bot, message: Message):
    log_file_path = "filesharingbot.txt"  # Log file name as specified in config.py
    
    if os.path.exists(log_file_path):
        await client.send_document(
            chat_id=message.chat.id,
            document=log_file_path,
            caption="Here are the bot logs."
        )
    else:
        await message.reply("Log file not found.")