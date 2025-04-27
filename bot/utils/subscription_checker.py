from database.manage_subs import get_subscription_channels
from aiogram.exceptions import TelegramBadRequest

async def is_subscribed(user_id):
    channels = await get_subscription_channels()
    for channel_id in channels:
        try:
            member = await bot.get_chat_member(channel_id, user_id)
            if member.status not in ["member", "administrator", "creator"]:
                return False
        except TelegramBadRequest:
            return False
    return True
