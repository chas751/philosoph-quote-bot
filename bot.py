import os
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я философский бот. Напиши /quote, чтобы получить цитату.")

@dp.message_handler(commands=['quote'])
async def send_quote(message: types.Message):
    quotes = [
        "Жизнь — это то, что с тобой происходит, пока ты строишь планы.",
        "Познай себя.",
        "Всё течёт, всё меняется."
    ]
    import random
    await message.reply(random.choice(quotes))

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)