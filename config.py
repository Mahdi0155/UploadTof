import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

OWNER_ID = int(os.getenv('OWNER_ID'))

ADMINS = list(map(int, os.getenv('ADMINS', '').split()))

CHANNEL_ID = int(os.getenv('CHANNEL_ID'))  # آیدی چنلی که فایل‌ها اونجا آپلود میشن

REQUIRED_CHANNELS = os.getenv('REQUIRED_CHANNELS', '').split()
REQUIRED_CHANNELS = [int(channel) for channel in REQUIRED_CHANNELS if channel]

ADMIN_FILE = os.getenv('ADMIN_FILE')

WEBHOOK_URL = "https://uploadtof.onrender.com/webhook"
