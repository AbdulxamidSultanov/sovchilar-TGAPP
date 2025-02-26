from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import Command
import asyncio

TOKEN = "8066095257:AAG9W4w2nyg6WKB7zHt1f-CQ8mtQJPis2wM"
WEB_APP_URL = "https://sovchilar-tgapp.vercel.app"  # Твоя ссылка

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton("Открыть веб-приложение", web_app=WebAppInfo(url=WEB_APP_URL))
    keyboard.add(button)

    await message.answer("Нажмите кнопку ниже, чтобы открыть веб-приложение:", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
