from config import REQUIRED_CHANNELS
from bot.utils.check_user import is_user_in_channel
from aiogram import Bot

async def is_subscribed(user_id: int, bot: Bot) -> bool:
    """
    چک می‌کند آیا کاربر در همه کانال‌های اجباری عضو شده یا نه
    """
    if not REQUIRED_CHANNELS:
        return True  # اگر کانالی ست نشده بود
    
    for channel_id in REQUIRED_CHANNELS:
        if not await is_user_in_channel(bot, user_id, channel_id):
            return False
    return True
