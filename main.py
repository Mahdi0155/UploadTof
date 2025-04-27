import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# اگر تابع فیلتر خاص داری، مثلا is_user_admin یا غیره، اینجا تعریفش کن یا ایمپورت کن.

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.reply("سلام! من آماده‌ام.")

@dp.message_handler(commands=["upload"])
async def upload_handler(message: types.Message):
    await message.reply("لطفاً فایلت رو بفرست!")

@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def handle_file(message: types.Message):
    document = message.document
    await message.reply(f"فایل {document.file_name} دریافت شد!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
