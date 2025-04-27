from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

def admin_main_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("➕ افزودن ادمین جدید"))
    keyboard.add(KeyboardButton("مدیریت فایل‌ها"))
    keyboard.add(KeyboardButton("تنظیم عضویت اجباری"))
    keyboard.add(KeyboardButton("ارسال فایل جدید"))
    return keyboard

def manage_files_keyboard(files):
    keyboard = InlineKeyboardMarkup()
    for file in files:
        keyboard.add(InlineKeyboardButton(text=f"{file['id']}. {file['name']}", callback_data=f"delete_file_{file['id']}"))
    return keyboard

def subscription_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="➕ افزودن کانال", callback_data="add_channel"))
    keyboard.add(InlineKeyboardButton(text="➖ حذف کانال", callback_data="remove_channel"))
    return keyboard

def send_file_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="✏️ ویرایش کپشن", callback_data="edit_caption"))
    keyboard.add(InlineKeyboardButton(text="✅ تایید ارسال", callback_data="confirm_send"))
    return keyboard
