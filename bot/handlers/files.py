from aiogram import Router, F
from aiogram.types import Message
from database.manage_files import save_file, get_file

router = Router()

@router.message(F.document)
async def handle_document(message: Message):
    file_id = message.document.file_id
    file_unique_id = message.document.file_unique_id
    save_file(file_unique_id, file_id)
    await message.answer("فایل شما ذخیره شد.")

@router.message(F.text.startswith("/getfile_"))
async def send_document(message: Message):
    file_unique_id = message.text.split("_", 1)[1]
    file_id = get_file(file_unique_id)
    if file_id:
        await message.answer_document(file_id)
    else:
        await message.answer("فایلی با این شناسه پیدا نشد.")
