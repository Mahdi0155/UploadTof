from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from bot.keyboards.admin_keyboards import admin_main_keyboard
from bot.keyboards.admin_keyboards import manage_files_keyboard
from bot.keyboards.admin_keyboards import subscription_keyboard
from bot.keyboards.admin_keyboards import send_file_keyboard
from bot.utils.file_manager import list_files, delete_file
from bot.utils.caption_editor import build_caption
from bot.utils.channel_manager import add_channel, remove_channel
from database.manage_admins import is_owner, add_admin
from database.manage_subs import add_subscription_channel, remove_subscription_channel

router = Router()

@router.message(F.text == "➕ افزودن ادمین جدید")
async def add_admin_handler(message: Message):
    if not await is_owner(message.from_user.id):
        return
    await message.answer("آیدی عددی ادمین جدید را ارسال کنید:")

@router.message(F.text == "مدیریت فایل‌ها")
async def manage_files_handler(message: Message):
    files = list_files()
    if not files:
        await message.answer("هیچ فایلی موجود نیست.")
        return
    await message.answer("فایل‌های موجود:", reply_markup=manage_files_keyboard(files))

@router.callback_query(F.data.startswith("delete_file_"))
async def delete_file_handler(callback: CallbackQuery):
    file_id = callback.data.split("_")[-1]
    delete_file(file_id)
    await callback.answer("فایل حذف شد.", show_alert=True)
    await callback.message.delete()

@router.message(F.text == "تنظیم عضویت اجباری")
async def subscription_handler(message: Message):
    await message.answer("لینک کانال جدید را ارسال کنید یا برای حذف لینک اقدام کنید.", reply_markup=subscription_keyboard())

@router.message(F.text == "ارسال فایل جدید")
async def send_file_handler(message: Message):
    await message.answer("لطفا فایل خود را ارسال کنید.", reply_markup=send_file_keyboard())
