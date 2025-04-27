from aiogram import Router, F
from aiogram.types import Message
from bot.utils.subscription_checker import is_subscribed
from bot.utils.file_sender import send_temp_file

router = Router()

@router.message(F.text == "/start")
async def start_handler(message: Message):
    if await is_subscribed(message.from_user.id):
        await message.answer("سلام خوش اومدی! فایل خودتو اینجا دریافت کن.")
        await send_temp_file(message)
    else:
        await message.answer("⚠️ برای استفاده از ربات ابتدا در کانال عضو شو سپس /start رو بزن.")
