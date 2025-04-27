import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
OWNER_ID = int(os.getenv('OWNER_ID'))
ADMINS = list(map(int, os.getenv('ADMINS').split()))
CHANNEL_ID = -1002207109791  # کانالی که فایل رو اونجا میفرسته
REQUIRED_CHANNELS = list(map(int, os.getenv('REQUIRED_CHANNELS').split()))
ADMIN_FILE = os.getenv('ADMIN_FILE')
WEBHOOK_URL = "https://uploadtof.onrender.com/webhook"
