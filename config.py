import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
OWNER_ID = int(os.getenv('OWNER_ID', 0))  # اگر نبود 0 میزاره
ADMINS = list(map(int, os.getenv('ADMINS', '0').split())) if os.getenv('ADMINS') else []
CHANNEL_ID = int(os.getenv('CHANNEL_ID', 0))  # اگر نبود 0 میزاره
ADMIN_FILE = os.getenv('ADMIN_FILE')
WEBHOOK_URL = "https://uploadtof.onrender.com/webhook"

# پردازش کانال‌های اجباری
REQUIRED_CHANNELS = os.getenv('REQUIRED_CHANNELS', '').split()
REQUIRED_CHANNELS = [int(channel) for channel in REQUIRED_CHANNELS if channel]
