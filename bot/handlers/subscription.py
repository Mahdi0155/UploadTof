from aiogram import Router, F
from aiogram.types import Message
from database.manage_channels import add_channel, remove_channel
from bot.keyboards.subscription_management import subscription_menu
from config import OWNER_ID

router = Router()

@router.message(F.text == "🔗 تنظیم عضویت اجباری")
async def open_subscription_menu(message: Message):
    if str(message.from_user.id) != OWNER_ID:
        return
    await message.answer("مدیریت عضویت اجباری:", reply_markup=subscription_menu())

@router.message(F.text == "➕ اضافه کردن کانال")
async def ask_channel_add(message: Message):
    if str(message.from_user.id) != OWNER_ID:
        return
    await message.answer("آیدی عددی کانال را ارسال کنید.")

@router.message(F.text == "➖ حذف کردن کانال")
async def ask_channel_remove(message: Message):
    if str(message.from_user.id) != OWNER_ID:
        return
    await message.answer("آیدی عددی کانال موردنظر برای حذف را ارسال کنید.")

@router.message(lambda message: message.text.isdigit())
async def handle_channel_operations(message: Message):
    if str(message.from_user.id) != OWNER_ID:
        return
    channel_id = message.text
    if add_channel(channel_id):
        await message.answer(f"✅ کانال {channel_id} اضافه شد.", reply_markup=subscription_menu())
    elif remove_channel(channel_id):
        await message.answer(f"➖ کانال {channel_id} حذف شد.", reply_markup=subscription_menu())
