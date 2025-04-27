from aiogram import Router, F
from aiogram.types import Message
from bot.keyboards.admin import admin_main_menu
from database.manage_admins import is_owner

router = Router()

@router.message(F.text == "پنل مدیریت")
async def admin_panel_handler(message: Message):
    if not await is_owner(message.from_user.id):
        return
    await message.answer("به پنل مدیریت خوش آمدید.", reply_markup=admin_main_menu())
