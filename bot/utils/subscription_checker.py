from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest

async def is_user_in_channel(bot: Bot, user_id: int, channel_id: int) -> bool:
    """
    چک می‌کند آیا کاربر در کانال عضو است یا خیر
    """
    try:
        member = await bot.get_chat_member(chat_id=channel_id, user_id=user_id)
        return member.status in ("member", "administrator", "creator")
    except TelegramBadRequest:
        # مثلا کاربر بلاک کرده یا چت پیدا نشده
        return False
