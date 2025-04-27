from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from bot.keyboards.file_management import file_options
from bot.keyboards.file_confirmation import confirm_file_keyboard
from config import OWNER_ID
import asyncio

router = Router()
uploaded_files = {}

@router.message(F.text == "📤 ارسال فایل جدید")
async def ask_for_file(message: Message):
    if str(message.from_user.id) != OWNER_ID:
        return
    await message.answer("لطفا عکس یا ویدیو را ارسال کنید.")

@router.message(F.photo | F.video)
async def receive_file(message: Message):
    if str(message.from_user.id) != OWNER_ID:
        return
    file_id = message.photo[-1].file_id if message.photo else message.video.file_id
    uploaded_files[message.from_user.id] = {"file_id": file_id}
    await message.answer("حالا کپشن فایل را ارسال کنید.")

@router.message(F.text & (lambda m: m.from_user.id in uploaded_files))
async def receive_caption(message: Message):
    if str(message.from_user.id) != OWNER_ID:
        return
    uploaded_files[message.from_user.id]["caption"] = message.text
    await message.answer_photo(
        uploaded_files[message.from_user.id]["file_id"],
        caption=f"{message.text}\n\n🔵 [مشاهده](https://t.me/{(await message.bot.get_me()).username})",
        parse_mode="Markdown",
        reply_markup=confirm_file_keyboard()
    )

@router.callback_query(F.data == "confirm_send")
async def confirm_send_file(callback_query: CallbackQuery):
    data = uploaded_files.get(callback_query.from_user.id)
    if not data:
        return
    await callback_query.message.answer("✅ فایل به کانال ارسال شد.")
    del uploaded_files[callback_query.from_user.id]

@router.callback_query(F.data == "edit_caption")
async def edit_caption(callback_query: CallbackQuery):
    await callback_query.message.answer("✏️ لطفا کپشن جدید را ارسال کنید.")
