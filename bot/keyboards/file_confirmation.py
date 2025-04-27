from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def confirm_file_keyboard():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton(text="✅ تایید و ارسال", callback_data="confirm_send"),
        InlineKeyboardButton(text="✏️ ویرایش کپشن", callback_data="edit_caption")
    )
    return kb
