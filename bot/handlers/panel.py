# bot/handlers/panel.py

from aiogram import Router, F
from aiogram.types import Message
from config import OWNER_ID
from bot.keyboards.admin_panel import admin_main_menu

router = Router()

@router.message(F.text == "/panel")
async def open_panel(message: Message):
    if message.from_user.id != OWNER_ID:
        await message.answer("❌ شما اجازه دسترسی به پنل مدیریت را ندارید.")
        return
    await message.answer("به پنل مدیریت خوش آمدید:", reply_markup=admin_main_menu())
