from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import random

# Загружаем токен из .env
load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет! 🌿 Я философский бот. Хочешь цитату мудреца? Напиши /quote")

@dp.message_handler(commands=["quote"])
async def send_quote(message: types.Message):
    quotes = [
        "Познай самого себя. — Сократ",
        "Мыслить — значит спорить с собой. — Аристотель",
        "Мудрый человек не говорит всё, что думает. — Сенека",
    ]
    await message.answer(random.choice(quotes))

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
