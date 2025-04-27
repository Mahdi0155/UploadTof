from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def subscription_menu():
    kb = [
        [KeyboardButton("➕ اضافه کردن کانال"), KeyboardButton("➖ حذف کردن کانال")],
        [KeyboardButton("🔙 بازگشت")]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
