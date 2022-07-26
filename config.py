# powerd by Beta
import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Beta-Music")
API_ID = int(getenv("API_ID", "8945070"))
API_HASH = getenv("API_HASH", "")
OWNER_ID = int(getenv("OWNER_ID", ""))
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")
LOG_ID = getenv("LOG_ID", "")

OWNER_NAME = getenv("OWNER_NAME", "JP_Jeol_org")
ALIVE_NAME = getenv("ALIVE_NAME", "JEOL")
BOT_USERNAME = getenv("BOT_USERNAME", "")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5372572893").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/BETA-OFFICIAL/BETA-MUSICBOT")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/13424efd47300f29dc31d.jpg")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/596f75a52ea9bf0109644.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/92e8c83e9148c6fea5f3b.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/92e8c83e9148c6fea5f3b.png")
DB_URL = getenv("DB_URL", "")
