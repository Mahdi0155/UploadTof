from aiogram import BaseMiddleware
from aiogram.types import Message
from config import REQUIRED_CHANNELS
from bot.utils.check_user import is_user_in_channel

class CheckSubscriptionMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Message, data: dict):
        if not hasattr(event, 'from_user') or event.from_user is None:
            return await handler(event, data)

        if not REQUIRED_CHANNELS:
            return await handler(event, data)

        for channel_id in REQUIRED_CHANNELS:
            if not await is_user_in_channel(event.bot, event.from_user.id, channel_id):
                await event.answer("⚠️ برای استفاده از ربات، لطفا ابتدا در کانال ما عضو شوید.")
                return  # جلوشو میگیریم که دستور اجرا نشه
        await handler(event, data)
