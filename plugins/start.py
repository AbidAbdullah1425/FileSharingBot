# Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport

import asyncio
import os
import random
import sys
import time
import string
import string as rohit
import humanize
from pyrogram import Client, filters, __version__
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated, UserNotParticipant
from bot import Bot
import config
from helper_func import *
from database.database import *
from plugins.Invite_links import export_invite_links
import importlib

# File auto-delete time in seconds (Set your desired time in seconds here)
FILE_AUTO_DELETE = config.TIME  # Example: 3600 seconds (1 hour)
TUT_VID = f"{config.TUT_VID}"

def reload_config():
    importlib.reload(config)

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

@Bot.on_message(filters.command('start') & filters.private & subscribed1 & subscribed2 & subscribed3 & subscribed4)
async def start_command(client: Client, message: Message):
    temp_msg = await message.reply("› › ᴡᴀɪᴛ ᴀ sᴇᴄᴏɴᴅ...")
    id = message.from_user.id
    if not await present_user(id):
        try:
            await add_user(id)
        except:
            pass

    # Check if user is an admin and treat them as verified
    if id in config.ADMINS:
        verify_status = {
            'is_verified': True,
            'verify_token': None,  # Admins don't need a token
            'verified_time': time.time(),
            'link': ""
        }
    else:
        verify_status = await get_verify_status(id)

        # If TOKEN is enabled, handle verification logic
        if config.TOKEN:
            if verify_status['is_verified'] and config.VERIFY_EXPIRE < (time.time() - verify_status['verified_time']):
                await update_verify_status(id, is_verified=False)

            if "verify_" in message.text:
                _, token = message.text.split("_", 1)
                if verify_status['verify_token'] != token:
                    return await message.reply("Your token is invalid or expired. Try again by clicking /start.")
                await update_verify_status(id, is_verified=True, verified_time=time.time())
                if verify_status["link"] == "":
                    reply_markup = None
                return await message.reply(
                    f"Your token has been successfully verified and is valid for {get_exp_time(config.VERIFY_EXPIRE)}",
                    reply_markup=reply_markup,
                    protect_content=False,
                    quote=True
                )

            if not verify_status['is_verified']:
                token = ''.join(random.choices(rohit.ascii_letters + rohit.digits, k=10))
                await update_verify_status(id, verify_token=token, link="")
                link = await get_shortlink(config.SHORTLINK_URL, config.SHORTLINK_API, f'https://telegram.dog/{client.username}?start=verify_{token}')
                btn = [
                    [InlineKeyboardButton("• ᴏᴘᴇɴ ʟɪɴᴋ •", url=link)],
                    [InlineKeyboardButton('• ʜᴏᴡ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋ •', url=TUT_VID)]
                ]
                
                return await message.reply(
                    f"<b>Your token has expired. Please refresh your token to continue.\n\nToken Timeout: {get_exp_time(config.VERIFY_EXPIRE)}\n\nWhat is the token?\n\nThis is an ads token. Passing one a[...",
                    reply_markup=InlineKeyboardMarkup(btn),
                    protect_content=False,
                    quote=True
                )

    # Handle normal message flow
    text = message.text
    if len(text) > 7:
        try:
            base64_string = text.split(" ", 1)[1]
        except IndexError:
            return

        string = await decode(base64_string)
        argument = string.split("-")

        ids = []
        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(client.db_channel.id))
                end = int(int(argument[2]) / abs(client.db_channel.id))
                ids = range(start, end + 1) if start <= end else list(range(start, end - 1, -1))
            except Exception as e:
                print(f"Error decoding IDs: {e}")
                return

        elif len(argument) == 2:
            try:
                ids = [int(int(argument[1]) / abs(client.db_channel.id))]
            except Exception as e:
                print(f"Error decoding ID: {e}")
                return

        
        try:
            messages = await get_messages(client, ids)
        except Exception as e:
            await message.reply_text("Something went wrong!")
            print(f"Error getting messages: {e}")
            return
        finally:
            await temp_msg.delete()

        codeflix_msgs = []
        for msg in messages:
            caption = (config.CUSTOM_CAPTION.format(previouscaption="" if not msg.caption else msg.caption.html, 
                                                     filename=msg.document.file_name) if bool(config.CUSTOM_CAPTION) and bool(msg.document)
                       else ("" if not msg.caption else msg.caption.html))

            reply_markup = msg.reply_markup if config.DISABLE_CHANNEL_BUTTON else None

            try:
                copied_msg = await msg.copy(chat_id=message.from_user.id, caption=caption, parse_mode=ParseMode.HTML, 
                                            reply_markup=reply_markup, protect_content=config.PROTECT_CONTENT)
                codeflix_msgs.append(copied_msg)
            except FloodWait as e:
                await asyncio.sleep(e.x)
                copied_msg = await msg.copy(chat_id=message.from_user.id, caption=caption, parse_mode=ParseMode.HTML, 
                                            reply_markup=reply_markup, protect_content=config.PROTECT_CONTENT)
                codeflix_msgs.append(copied_msg)
            except Exception as e:
                print(f"Failed to send message: {e}")
                pass

        if FILE_AUTO_DELETE > 0:
            notification_msg = await message.reply(
                f"<b><blockquote>This file will be deleted in {get_exp_time(FILE_AUTO_DELETE)}. Please save or forward it to your saved messages before it gets deleted.</blockquote></b>"
            )

            await asyncio.sleep(FILE_AUTO_DELETE)

            for snt_msg in codeflix_msgs:    
                if snt_msg:
                    try:    
                        await snt_msg.delete()  
                    except Exception as e:
                        print(f"Error deleting message {snt_msg.id}: {e}")

            try:
                reload_url = (
                    f"https://t.me/{client.username}?start={message.command[1]}"
                    if message.command and len(message.command) > 1
                    else None
                )
                keyboard = InlineKeyboardMarkup(
                    [[InlineKeyboardButton("• ɢᴇᴛ ғɪʟᴇs •", url=reload_url), InlineKeyboardButton("ᴄʟᴏsᴇ •", callback_data="close")]]
                ) if reload_url else None

                await notification_msg.edit(
                    f"<b><blockquote>›› Pʀᴇᴠɪᴏᴜs Mᴇssᴀɢᴇ ᴡᴀs Dᴇʟᴇᴛᴇᴅ !!\n\n"
                    f"Iғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ғɪʟᴇs ᴀɢᴀɪɴ, ᴛʜᴇɴ ᴄʟɪᴄᴋ: "
                    f"<a href='{reload_url}'>• ɢᴇᴛ ғɪʟᴇs •</a> ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴇʟsᴇ ᴄʟᴏsᴇ ᴛʜɪs ᴍᴇssᴀɢᴇ.</blockquote></b>",
                    reply_markup=keyboard,
                    disable_web_page_preview=True
                )
            except Exception as e:
                print(f"Error updating notification with 'Get File Again' button: {e}")
    else:
        reply_markup = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("• ᴀʙᴏᴜᴛ •", callback_data="about")]
            ]
        )
        await message.reply_photo(
            photo=config.START_PIC,
            caption=config.START_MSG.format(
                first=message.from_user.first_name,
                last=message.from_user.last_name,
                username=None if not message.from_user.username else '@' + message.from_user.username,
                mention=message.from_user.mention,
                id=message.from_user.id
            ),
            reply_markup=reply_markup#,
            #message_effect_id=5104841245755180586  # 🔥
        )

#=====================================================================================##
# Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport

@Bot.on_message(filters.command('start') & filters.private)
async def not_joined(client: Client, message: Message):
    wait_msg = await message.reply("› › ᴡᴀɪᴛ ᴀ sᴇᴄᴏɴᴅ...")

    reload_config()

    # Generate invite links using the function from Invite_links.py
    await export_invite_links(client)

    # Initialize buttons list
    buttons = []

    # Check and append buttons based on the config.FORCE_SUB_CHANNEL values
    if config.FORCE_SUB_CHANNEL1 != 0:
        buttons.append([InlineKeyboardButton(text="• ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ •", url=client.invitelink1)])
    if config.FORCE_SUB_CHANNEL2 != 0:
        buttons.append([InlineKeyboardButton(text="• ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ •", url=client.invitelink2)])
    if config.FORCE_SUB_CHANNEL3 != 0:
        buttons.append([InlineKeyboardButton(text="• ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ •", url=client.invitelink3)])
    if config.FORCE_SUB_CHANNEL4 != 0:
        buttons.append([InlineKeyboardButton(text="• ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ •", url=client.invitelink4)])

    # Append "Try Again" button if the command has a second argument
    try:
        buttons.append([
            InlineKeyboardButton(
                text="ʀᴇʟᴏᴀᴅ",
                url=f"https://t.me/{client.username}?start={message.command[1]}"
            )
        ])
    except IndexError:
        pass  # Ignore if no second argument is present

    await message.reply_photo(
        photo=config.FORCE_PIC,
        caption=config.FORCE_MSG.format(
            first=message.from_user.first_name,
            last=message.from_user.last_name,
            username=None if not message.from_user.username else '@' + message.from_user.username,
            mention=message.from_user.mention,
            id=message.from_user.id
        ),
        reply_markup=InlineKeyboardMarkup(buttons)
    )
    await wait_msg.delete()