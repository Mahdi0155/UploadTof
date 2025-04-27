from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def file_options(file_id):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("❌ حذف فایل", callback_data=f"delete_file:{file_id}"))
    return kb
