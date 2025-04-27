from aiogram import Router, F
from aiogram.types import Message
from database.manage_subscribers import subscribe_user

router = Router()

@router.message(F.text == "/start")
async def start(message: Message):
    subscribe_user(message.from_user.id)
    await message.answer("به ربات خوش آمدید!")
