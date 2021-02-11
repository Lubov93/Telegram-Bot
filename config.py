import os
from dotenv import load_dotenv


load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
URL_STROYS = os.getenv("URL_STROYS")
URL_REMONTS = os.getenv("URL_REMONTS")


print(BOT_TOKEN)