from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest

async def is_user_in_channel(bot: Bot, user_id: int, channel_id: str):
    try:
        member = await bot.get_chat_member(chat_id=channel_id, user_id=user_id)
        return member.status in ("member", "administrator", "creator")
    except TelegramBadRequest:
        return False
