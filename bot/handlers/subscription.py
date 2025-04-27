from aiogram import BaseMiddleware
from aiogram.types import Message
from config import REQUIRED_CHANNELS
from utils.check_user import is_user_in_channel

class CheckSubscriptionMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Message, data: dict):
        if not REQUIRED_CHANNELS:
            return await handler(event, data)

        for channel_id in REQUIRED_CHANNELS:
            if not await is_user_in_channel(event.bot, event.from_user.id, channel_id):
                await event.answer("⚠️ برای دریافت فایل‌ها، ابتدا باید در کانال‌های ما عضو شوید.")
                return
        await handler(event, data)
