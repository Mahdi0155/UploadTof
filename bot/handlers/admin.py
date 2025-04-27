from aiogram import Router, F
from aiogram.types import Message
from config import OWNER_ID
from bot.keyboards.admin_keyboards import admin_main_menu
from database.manage_admins import add_admin, is_owner

router = Router()

@router.message(F.text == "➕ افزودن ادمین جدید")
async def add_admin_handler(message: Message):
    if not is_owner(message.from_user.id):
        return
    await message.answer("لطفا آیدی عددی ادمین جدید را ارسال کنید.")

@router.message(lambda message: message.text.isdigit())
async def save_admin_id(message: Message):
    if not is_owner(message.from_user.id):
        return
    success = add_admin(int(message.text))
    if success:
        await message.answer("✅ ادمین جدید اضافه شد.", reply_markup=admin_main_menu())
    else:
        await message.answer("⚠️ این ادمین قبلا اضافه شده.", reply_markup=admin_main_menu())

@router.message(F.text == "🔙 بازگشت به منو اصلی")
async def back_to_main(message: Message):
    if not is_owner(message.from_user.id):
        return
    await message.answer("به منوی اصلی برگشتید.", reply_markup=admin_main_menu())
