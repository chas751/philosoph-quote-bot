import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

quotes = [
    "Жизнь — это то, что происходит, пока вы строите планы.",
    "Мысли формируют реальность.",
    "Каждое утро — это шанс начать заново."
]

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот, который присылает философские цитаты каждый день.")

@dp.message_handler(commands=['quote'])
async def send_quote(message: types.Message):
    import random
    await message.reply(random.choice(quotes), parse_mode=ParseMode.HTML)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
