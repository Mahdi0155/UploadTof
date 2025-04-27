# main.py

import asyncio
from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web
from config import BOT_TOKEN, WEBHOOK_URL
from bot.handlers import admin_panel, admin, files, subscription
from bot.middlewares.check_subscription import CheckSubscriptionMiddleware

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()

# اضافه کردن middleware بررسی عضویت
dp.update.middleware(CheckSubscriptionMiddleware())

# ثبت تمام روت‌ها (دستورات)
dp.include_routers(
    admin_panel.router,
    admin.router,
    files.router,
    subscription.router,
)

# اجرای عملیات در شروع برنامه
async def on_startup(app):
    await bot.set_webhook(WEBHOOK_URL)

# اجرای عملیات هنگام خاموش شدن برنامه
async def on_shutdown(app):
    await bot.delete_webhook()

# تابع اصلی برای راه‌اندازی سرور وبهوک
async def main():
    app = web.Application()
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path="/webhook")
    setup_application(app, dp, bot=bot)

    return app

# اجرای برنامه
if __name__ == "__main__":
    web.run_app(main(), host="0.0.0.0", port=10000)
