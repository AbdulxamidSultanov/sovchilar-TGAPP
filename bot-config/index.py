from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

TOKEN = "8066095257:AAG9W4w2nyg6WKB7zHt1f-CQ8mtQJPis2wM"
WEB_APP_URL = "https://sovchilar-tgapp.vercel.app"  # Ссылка на твою веб-страницу

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton("Открыть веб-приложение", web_app=types.WebAppInfo(url=WEB_APP_URL))
    keyboard.add(button)

    await message.answer("Нажмите кнопку ниже, чтобы открыть веб-приложение:", reply_markup=keyboard)

import asyncio

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(dp.start_polling())

