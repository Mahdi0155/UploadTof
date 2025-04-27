import asyncio
import os
from aiogram.types import Message
from bot.utils.file_manager import FILES_DIR

async def send_temp_file(message: Message):
    files = os.listdir(FILES_DIR)
    if not files:
        await message.answer("هیچ فایلی موجود نیست.")
        return

    file_path = os.path.join(FILES_DIR, files[-1])
    sent_message = await message.answer_document(open(file_path, "rb"))

    await asyncio.sleep(15)
    await sent_message.delete()
