from config import REQUIRED_CHANNELS
from bot.utils.check_user import is_user_in_channel

async def is_subscribed(user_id):
    from bot.main import bot  # دقت کن اینو اضافه میکنیم

    if not REQUIRED_CHANNELS:
        return True

    for channel_id in REQUIRED_CHANNELS:
        if not await is_user_in_channel(bot, user_id, channel_id):
            return False
    return True
