import sys
from bot import Bot
from config import OWNER_ID
from pyrogram import Client, filters

@Bot.on_message(filters.private & filters.command('restart') & filters.user(OWNER_ID))
async def restart_bot(client: Bot, message: Message):
    await message.reply("Restarting the bot...")
    os.execv(sys.executable, ['python'] + sys.argv)