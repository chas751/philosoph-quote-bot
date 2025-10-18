import os
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

# Load .env so the included BOT_TOKEN will be read (or Render environment variable BOT_TOKEN)
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN not set. Add it to .env or Render Environment Variables.")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.reply("Привет! Я философский бот. Напиши /quote")

@dp.message_handler(commands=['quote'])
async def cmd_quote(message: types.Message):
    quotes = [
        "Познай самого себя. — Сократ",
        "Мы то, что мы многократно делаем. — Аристотель",
        "Жизнь — это то, что с тобой происходит, пока ты строишь планы. — Джон Леннон",
    ]
    import random
    await message.reply(random.choice(quotes))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
