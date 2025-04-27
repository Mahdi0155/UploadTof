from database.manage_subs import add_subscription_channel, remove_subscription_channel

async def add_channel(link):
    await add_subscription_channel(link)

async def remove_channel(link):
    await remove_subscription_channel(link)
