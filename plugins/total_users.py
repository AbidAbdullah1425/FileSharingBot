import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from bot import Bot
from config import ADMINS
from database.database import full_userbase



WAIT_MSG = "<b>ᴡᴏʀᴋɪɴɢ....</b>"

@Bot.on_message(filters.command('users') & filters.private & filters.user(ADMINS))
async def get_users(client: Bot, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text=WAIT_MSG)
    users = await full_userbase()
    await msg.edit(f"{len(users)} users are using this bot")