from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import CHANNEL_LINK

def subscription_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="عضویت در کانال", url=CHANNEL_LINK)],
        [InlineKeyboardButton(text="بررسی عضویت ✅", callback_data="check_subscription")]
    ])
    return keyboard
