from aiogram import Router, F
from aiogram.types import Message
from config import CHANNEL_ID
from bot.keyboards.subscription import subscription_keyboard
from utils.subscription_checker import check_user_subscription

router = Router()

@router.message(F.text == "✅ بررسی عضویت")
async def check_subscription(message: Message):
    is_subscribed = await check_user_subscription(message.bot, message.from_user.id)
    if is_subscribed:
        await message.answer("شما در کانال عضو هستید. می‌توانید از ربات استفاده کنید.")
    else:
        await message.answer("شما هنوز در کانال عضو نشده‌اید!", reply_markup=subscription_keyboard())
