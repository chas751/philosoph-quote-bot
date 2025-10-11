import telebot
import time
import random
import threading
from PIL import Image, ImageDraw, ImageFont
import io

# 🔑 Твой токен
TOKEN = "8357091966:AAE_bsrgQAvwjb410w3vk7lLd2Dq6rxCheU"
bot = telebot.TeleBot(TOKEN)

# 📜 Цитаты
quotes = [
    'Познай самого себя. — Сократ',
    'Я мыслю, следовательно, я существую. — Декарт',
    'Мужество — это знать, чего не стоит бояться. — Платон',
    'Человек становится тем, о чём он думает весь день. — Эмерсон',
    'Мудрый человек не говорит всё, что думает. — Аристотель',
    'Если хочешь быть счастливым — будь им. — Толстой',
    'Свобода начинается с внутренней независимости. — Сенека'
]

# 🎨 Генерация изображения с цитатой
def generate_quote_image(text):
    img = Image.new('RGB', (1080, 1080), color=(245, 222, 179))  # фон пергамента
    draw = ImageDraw.Draw(img)

    # Заголовок
    title = "📜 Мудрость дня"
    font_title = ImageFont.truetype("arial.ttf", 60)
    font_text = ImageFont.truetype("arial.ttf", 50)

    # Рисуем текст
    draw.text((100, 80), title, font=font_title, fill=(80, 50, 20))
    draw.text((100, 300), text, font=font_text, fill=(40, 30, 10))

    # Преобразуем в байты
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes.seek(0)
    return img_bytes

# Счётчик публикаций
post_counter = 0

# 🕊️ Отправка цитаты
def send_quote():
    global post_counter
    post_counter += 1

    quote = random.choice(quotes)
    img = generate_quote_image(quote)

    # Каждая 5-я публикация — с реквизитами
    if post_counter % 5 == 0:
        caption = "💬 Поддержать проект:\n💳 ВТБ: 2200 2460 3013 9912"
    else:
        caption = ""

    bot.send_photo("@daily_philosoph", img, caption=caption)

# 🔁 Автоматическая отправка каждые 2 часа
def schedule_quotes():
    while True:
        send_quote()
        time.sleep(7200)  # каждые 2 часа

# 🚀 Запуск фонового потока
threading.Thread(target=schedule_quotes, daemon=True).start()

# ✋ Ручная публикация
@bot.message_handler(commands=['quote'])
def manual_post(message):from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is running!"

def run_flask():
    app.run(host='0.0.0.0', port=10000)

if __name__ == "__main__":
    import threading
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # твой код бота ниже
    import telebot
    from config import TOKEN

    bot = telebot.TeleBot(TOKEN)

    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, "Привет! Бот работает на Render!")

    bot.polling(none_stop=True)

    send_quote()
    bot.reply_to(message, "Новая цитата опубликована!")

# ▶️ Запуск бота
bot.polling(none_stop=True)
