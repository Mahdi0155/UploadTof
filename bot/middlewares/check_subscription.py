from aiogram import BaseMiddleware
from aiogram.types import Message
from bot.utils.subscription_checker import is_subscribed

class CheckSubscriptionMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Message, data: dict):
        if not hasattr(event, 'from_user') or event.from_user is None:
            return await handler(event, data)

        if not await is_subscribed(event.from_user.id, event.bot):
            await event.answer("⚠️ برای استفاده از ربات ابتدا در کانال(های) ما عضو شوید.")
            return

        await handler(event, data)
