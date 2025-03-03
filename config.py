# Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport


import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler
from pymongo import MongoClient


#rohit_1888 on Tg

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7542241757:")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "26254064"))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "72541d6610ae7730e6135af9423b319c")
#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002279496397"))
# NAMA OWNER
OWNER = os.environ.get("OWNER", "Noco")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5296584067"))
#Port
PORT = os.environ.get("PORT", "8030")
#Database
DB_URL = os.environ.get("DB_URL", "mongodb+srv://teamprosperpay:AbidAbdullah199@cluster0.z93fita.mongodb.net/")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#Time in seconds for message delete, put 0 to never delete
TIME = int(os.environ.get("TIME", "3600"))

client = MongoClient(DB_URL)
db = client[DB_NAME]
collection = db['force_sub_channels']

#remember default should exist or InlineKeyboardMarkup or SendMedia error can cause

FORCE_SUB_CHANNEL1 = int(os.getenv("FORCE_SUB_CHANNEL1", "-1002462572661"))
FORCE_SUB_CHANNEL2 = int(os.getenv("FORCE_SUB_CHANNEL2", "-1002355785538"))
FORCE_SUB_CHANNEL3 = int(os.getenv("FORCE_SUB_CHANNEL3", "-1002386614375"))
FORCE_SUB_CHANNEL4 = int(os.getenv("FORCE_SUB_CHANNEL4", "-1002315395252"))



def load_settings():
    for i in range(1, 5):
        setting = collection.find_one({"_id": f"FORCE_SUB_CHANNEL{i}"})
        os.environ[f"FORCE_SUB_CHANNEL{i}"] = str(setting["value"]) if setting else "0"
        globals()[f"FORCE_SUB_CHANNEL{i}"] = int(os.environ[f"FORCE_SUB_CHANNEL{i}"])

load_settings()

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://envs.sh/FVk.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://envs.sh/FVU.jpg")
ADMIN_PIC = os.environ.get("ADMIN_PIC", "https://envs.sh/_BZ.jpg")


# Turn this feature on or off using True or False put value inside  ""
# TRUE for yes FALSE if no 
TOKEN = True if os.environ.get('TOKEN', "True") == "False" else False 
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "publicearn.online")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "adabe1c0675be8ffc5ccbc84a9a65bc5a5d3ec69")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 0)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "False")
TUT_VID = os.environ.get("TUT_VID","https://t.me/hwdownload/3")


HELP_TXT = "<b><blockquote>ᴛʜɪs ɪs ᴀɴ ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ ᴡᴏʀᴋ ғᴏʀ @otakuflix_network\n\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n├/about : ᴏᴜʀ Iɴғᴏʀᴍᴀᴛɪᴏɴ\n└/help : ʜᴇʟᴘ ʀᴇʟᴀᴛᴇᴅ ʙᴏᴛ\n\n sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!\n\n ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ <a href=https://t.me/cosmic_freak>sᴜʙᴀʀᴜ</a></blockquote></b>"


ABOUT_TXT = "<b><blockquote>» ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/NocoWhiz>Nᴏᴄᴏ</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/HeavenlySubs>HᴇᴀᴠᴇɴʟʏSᴜʙs</a>\n◈ ᴄʜᴀᴛ ɢʀᴏᴜᴘ : <a href=https://t.me/HeavenlySubsChat>Gʀᴏᴜᴘ</a>\n◈ sᴘᴏɪʟᴇʀs & ᴘʀᴇᴠɪᴇᴡs : <a href=https://t.me/SpoilersPreviews_HS>Jᴏɪɴ Nᴏᴡ</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/NocoWhiz>Nᴏᴄᴏ</a></blockquote></b>"


START_MSG = os.environ.get("START_MESSAGE", "<b>Iʏʏʏᴀᴀᴀᴀᴀ {first}\n\n<blockquote>ɪ ᴄᴀɴ ɢɪᴠᴇ ʏᴏᴜ ʟᴀᴛᴇsᴛ ʙᴀᴛᴛʟᴇ ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ʜᴇᴀᴠᴇɴs ᴇᴘɪsᴏᴅᴇs.</blockquote></b>")

try:
    ADMINS=[5296584067]
    for x in (os.environ.get("ADMINS", "5296584067").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}\n\n<b><blockquote>ᴊᴏɪɴ ʙᴇʟᴏᴡ ᴄʜᴀɴɴᴇʟs ᴛʜᴇɴ ᴘʀᴇss ʀᴇʟᴏᴀᴅ ʙᴜᴛᴛᴏɴ.ɪ ᴡɪʟʟ ʙᴇ ᴛʜᴇʀᴇ ᴡɪᴛʜ ʏᴏᴜʀ ᴇᴘɪsᴏᴅᴇ.</b></blockquote>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "ᴇɴᴄᴏᴅᴇᴅ ʙʏ <a href='https://t.me/HeavenlySubs'>ʜᴇᴀᴠᴇɴʟʏ sᴜʙs</a>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ɪ ᴀᴍ ɴᴏᴛ ʏᴏᴜʀ ɢғ ᴅᴏɴᴏᴛ sᴇɴᴅ ᴍᴇ ᴍᴇssᴀɢᴇ.ᴍʏ ʙᴏʏғʀɪᴇɴᴅ » @NocoWhiz!!"

ADMINS.append(OWNER_ID)
ADMINS.append(5296584067)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   