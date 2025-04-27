from aiogram import BaseMiddleware
from aiogram.types import Message
from config import REQUIRED_CHANNELS
from bot.utils.check_user import is_user_in_channel

class CheckSubscriptionMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Message, data: dict):
        # اگر event کاربر نداشت بیخیال شو
        if not hasattr(event, 'from_user') or event.from_user is None:
            return await handler(event, data)

        # اگر لیست کانال های اجباری خالی بود، مستقیم برو ادامه
        if not REQUIRED_CHANNELS:
            return await handler(event, data)

        # چک کردن عضویت کاربر در همه کانال‌ها
        for channel_id in REQUIRED_CHANNELS:
            is_member = await is_user_in_channel(event.bot, event.from_user.id, channel_id)
            if not is_member:
                await event.answer("⚠️ برای استفاده از ربات باید در کانال عضو شوید.")
                return  # اگر عضو نبود، دیگه ادامه نده
        
        # اگر همه اوکی بود، درخواست بره مرحله بعد
        await handler(event, data)
