from aiogram import Router, F
from aiogram.types import Message
from bot.keyboards.admin import admin_main_menu
from database.manage_admins import is_admin

router = Router()

@router.message(F.text == "/panel")
async def panel_command(message: Message):
    if not await is_admin(message.from_user.id):
        await message.answer("❌ شما دسترسی به پنل ادمین ندارید.")
        return
    await message.answer("به پنل مدیریت خوش آمدید.", reply_markup=admin_main_menu())
