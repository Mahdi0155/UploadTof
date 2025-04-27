import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = os.getenv("OWNER_ID")
REQUIRED_CHANNELS = os.getenv("REQUIRED_CHANNELS", "").split(",")
