from aiogram import BaseMiddleware
from aiogram.types import Message
from utils.subscription_checker import check_user_subscription

class CheckSubscriptionMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Message, data: dict):
        if event.text in ["✅ بررسی عضویت", "📁 مشاهده فایل‌های من", "➕ افزودن ادمین جدید", "🔙 بازگشت به منو اصلی"]:
            return await handler(event, data)

        is_subscribed = await check_user_subscription(event.bot, event.from_user.id)
        if not is_subscribed:
            await event.answer("ابتدا باید در کانال عضو شوید تا بتوانید از ربات استفاده کنید.")
            return
        await handler(event, data)
