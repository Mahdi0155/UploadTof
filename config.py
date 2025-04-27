import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# اصلاح شده برای جلوگیری از ارور
channel_id = os.getenv("CHANNEL_ID")
if channel_id is None:
    raise ValueError("CHANNEL_ID environment variable not set.")
CHANNEL_ID = int(channel_id)
