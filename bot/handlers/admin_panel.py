from aiogram import Router, F
from aiogram.types import Message
from config import OWNER_ID
from bot.keyboards.admin_panel import admin_main_menu

router = Router()

@router.message(F.text == "/panel")
async def admin_panel(message: Message):
    if message.from_user.id != OWNER_ID:
        return
    await message.answer("به پنل ادمین خوش آمدید.", reply_markup=admin_main_menu())
