from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def admin_main_menu():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="➕ افزودن ادمین جدید")],
            [KeyboardButton(text="📁 مشاهده فایل‌های من")],
            [KeyboardButton(text="🔙 بازگشت به منو اصلی")]
        ],
        resize_keyboard=True
    )
    return keyboard
