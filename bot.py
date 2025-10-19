import os
import random
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    # If the TOKEN is not found in env, try .env file (for local use)
    from dotenv import load_dotenv
    load_dotenv()
    TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

quotes = [
    "Познай самого себя. — Сократ",
    "Мыслить — значит спорить с собой. — Аристотель",
    "Мудрый человек не говорит всё, что думает. — Сенека",
    "Жизнь — это то, что с тобой происходит, пока ты строишь планы. — Джон Леннон",
    "Каждое утро — это шанс начать заново."
]

@dp.message_handler(commands=['start','help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я философ-бот. Напиши /quote чтобы получить цитату.")

@dp.message_handler(commands=['quote'])
async def send_quote(message: types.Message):
    await message.reply(random.choice(quotes))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)