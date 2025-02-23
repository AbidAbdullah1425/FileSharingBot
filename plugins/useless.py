from bot import Bot
from pyrogram.types import Message
from pyrogram import filters
from config import ADMINS, BOT_STATS_TEXT, USER_REPLY_TEXT
from datetime import datetime, timedelta
from helper_func import get_readable_time

# Dictionary to store the last message time for each user
last_message_time = {}

# Cooldown period in seconds
COOLDOWN_PERIOD = 10

@Bot.on_message(filters.command('uptime') & filters.user(ADMINS))
async def stats(bot: Bot, message: Message):
    now = datetime.now()
    delta = now - bot.uptime
    time = get_readable_time(delta.seconds)
    await message.reply(BOT_STATS_TEXT.format(uptime=time))


@Bot.on_message(filters.private & filters.incoming)
async def useless(_, message: Message):
    global last_message_time

    user_id = message.from_user.id
    now = datetime.now()

    # Check if the user is in the dictionary and if they are within the cooldown period
    if user_id in last_message_time:
        last_time = last_message_time[user_id]
        if now - last_time < timedelta(seconds=COOLDOWN_PERIOD):
            return  # Ignore message if within cooldown period

    # Update the last message time for the user
    last_message_time[user_id] = now

    if USER_REPLY_TEXT:
        await message.reply(USER_REPLY_TEXT)