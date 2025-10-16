from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import random
from threading import Thread
from flask import Flask

# Загрузка токена
load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Основные команды
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(
        "Привет! 🌿 Я философский бот.\n"
        "Хочешь цитату мудреца? Напиши /quote"
    )

@dp.message_handler(commands=["quote"])
async def send_quote(message: types.Message):
    quotes = [
        "Познай самого себя. — Сократ",
        "Мыслить — значит спорить с собой. — Аристотель",
        "Мудрый человек не говорит всё, что думает. — Сенека",
        "Судьба правит миром, но не нашими поступками. — Монтень",
        "Всё течёт, всё меняется. — Гераклит",
    ]
    await message.answer(random.choice(quotes))

# Фиктивный веб-сервер для Render Free
app = Flask("")

@app.route("/")
def index():
    return "Bot is running!"

@app.route("/healthz")
def health():
    return "OK"

def run_flask():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

# Запуск Flask в отдельном потоке
Thread(target=run_flask).start()

# Запуск бота через long polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
