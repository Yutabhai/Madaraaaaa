#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7006740293:AAF7_wLTOTmPinvJeCyMojsWAT2B4vp0s4o")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "23902408"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "6a36a4ef2f07d63aeba7b53b99c64d73")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002219424361"))

REQUEST_CHANNEL1 = int(os.environ.get("CHANNEL_ONE", "-1002173795861"))
REQUEST_CHANNEL2 = int(os.environ.get("CHANNEL_TWO", "-1002148699593"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7179837246"))

#Port
PORT = os.environ.get("PORT", "8090")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://mex:rex@cluster7.jrzowqz.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "jhattu")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

HELP_TXT = "<b>Hi Dude!\nThis is an file to link bot work for @Anime_Bloodline\n\n❏ Bot Cammands\n├/start : start the bot\n├/about : Our Information\n└/help : Help related Bot\n\n💥 Simply click on link and start the bot join both channels and try again thats it.....!\n\n🧑‍💻 Developed by <a href=https://t.me/ShadowKakashi>ઝꪋઝꪋઽꫝꪱ</a></b>"

ABOUT_TXT = "<b>⟦⟧ Hi There {first}!💫\n┏━━━━━━━❪❂❫━━━━━━━━\n◈ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/ShadowKakashi>ઝꪋઝꪋઽꫝꪱ</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/Anime_Bloodline>ANIME CHANNEL</a>\n◈ ANIME CHANNEL : <a href=https://t.me/Anime_Bloodline>ANIME CHANNEL</a>\n◈ Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>\n◈ ᴍʏ ꜱᴇʀᴠᴇʀ : <a href=https://dashboard.heroku.com>Heroku</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/ShadowKakashi>ઝꪋઝꪋઽꫝꪱ</a>\n┗━━━━━━━❪❂❫━━━━━━━━</b>"

START_PIC = os.environ.get("START_PIC", "https://envs.sh/ILN.jpg")

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜɪ ᴛʜᴇʀᴇ... {first}! 💥\n\nɪ ᴀᴍ ᴀ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ...!\nɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇꜱ ᴛʜʀᴏᴜɢʜ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ʟɪɴᴋ....!\nᴘᴏᴡᴇʀᴇᴅ ʙʏ - @Anime_Bloodline</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7179837246").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}!⚡\n\n🫧ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ʙᴏᴛʜ ᴏꜰ ᴏᴜʀ ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟꜱ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ...!")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "🚫Pʟᴇᴀꜱᴇ ᴅᴏɴ'ᴛ ᴍᴇꜱꜱᴀɢᴇ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ ɪ ᴀᴍ ᴏɴʟʏ ᴡᴏʀᴋ ꜰᴏʀ​ - @Movies_Series_Universe"

ADMINS.append(OWNER_ID)
ADMINS.append(7179837246)

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
