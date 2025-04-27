from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def admin_main_menu():
    kb = [
        [KeyboardButton("➕ افزودن ادمین جدید"), KeyboardButton("👤 مدیریت ادمین‌ها")],
        [KeyboardButton("📂 مدیریت فایل‌ها")],
        [KeyboardButton("🔗 تنظیم عضویت اجباری")],
        [KeyboardButton("📤 ارسال فایل جدید")],
        [KeyboardButton("🔙 بازگشت به منو اصلی")]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
