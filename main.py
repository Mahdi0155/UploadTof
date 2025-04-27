import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from bot.handlers import admin, files, subscription
from bot.middlewares.check_subscription import CheckSubscriptionMiddleware

async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    dp.update.middleware(CheckSubscriptionMiddleware())

    dp.include_routers(
        admin.router,
        files.router,
        subscription.router,
    )

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
