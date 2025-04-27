from aiogram import Router, F
from aiogram.types import Message, FSInputFile
import os

router = Router()

UPLOAD_DIR = "uploads"

@router.message(F.document)
async def handle_file_upload(message: Message):
    file = message.document
    file_path = os.path.join(UPLOAD_DIR, file.file_name)

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    await message.bot.download(file, destination=file_path)
    await message.answer("فایل شما با موفقیت ذخیره شد.")

@router.message(F.text == "📁 مشاهده فایل‌های من")
async def list_files(message: Message):
    if not os.path.exists(UPLOAD_DIR):
        await message.answer("هیچ فایلی آپلود نشده است.")
        return

    files = os.listdir(UPLOAD_DIR)
    if not files:
        await message.answer("هیچ فایلی موجود نیست.")
    else:
        text = "لیست فایل‌ها:\n\n" + "\n".join(files)
        await message.answer(text)

@router.message(F.text.startswith("دانلود "))
async def download_file(message: Message):
    filename = message.text.replace("دانلود ", "").strip()
    file_path = os.path.join(UPLOAD_DIR, filename)

    if not os.path.exists(file_path):
        await message.answer("فایلی با این نام پیدا نشد.")
        return

    await message.answer_document(FSInputFile(file_path))
