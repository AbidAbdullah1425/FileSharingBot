import sys
from bot import Bot
from pyrogram import Client, filters

@Bot.on_message(filters.private & filters.command('restart') & filters.user(ADMINS))
async def restart_bot(client: Bot, message: Message):
    await message.reply("Restarting the bot...")
    os.execv(sys.executable, ['python'] + sys.argv)