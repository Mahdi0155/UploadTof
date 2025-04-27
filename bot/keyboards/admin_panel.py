from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def admin_main_menu():
    keyboard = [
        [KeyboardButton(text="➕ افزودن ادمین جدید")],
        [KeyboardButton(text="📁 مدیریت فایل‌ها")],
        [KeyboardButton(text="👥 مدیریت اعضا")],
        [KeyboardButton(text="🔙 بازگشت به منو اصلی")],
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
