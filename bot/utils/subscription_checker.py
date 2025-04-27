from config import REQUIRED_CHANNELS
from aiogram import Bot

async def is_subscribed(user_id: int, bot: Bot) -> bool:
    if not REQUIRED_CHANNELS:
        return True

    for channel_id in REQUIRED_CHANNELS:
        try:
            member = await bot.get_chat_member(channel_id, user_id)
            if member.status not in ("member", "creator", "administrator"):
                return False
        except Exception:
            return False
    return True
