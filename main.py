import telebot
from flask import Flask, request
import logging
import os

# ====== ВАШ ТОКЕН ======
TOKEN = "8357091966:AAGdvUQnHejEjJ9B5RG69tNad9bVt7G-_1M"
# =======================

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# лог в stdout — будет виден в логах Render
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            json_str = request.get_data().decode('utf-8')
            logger.info("Incoming raw update: %s", json_str)
            update = telebot.types.Update.de_json(json_str)
            bot.process_new_updates([update])
        except Exception as e:
            logger.exception("Failed to process update: %s", e)
            return "ERR", 500
        return '', 200
    else:
        return 'Bot is alive!', 200

# simple /start handler
@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.send_message(message.chat.id, "✅ Привет! Бот запущен и готов. Напиши /quote чтобы получить цитату.")

# simple /quote handler (example)
@bot.message_handler(commands=['quote'])
def cmd_quote(message):
    bot.send_message(message.chat.id, "«Мудрость — это не запас знаний, а умение жить»")

# catch-all (echo) — временно, можно удалить
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.send_message(message.chat.id, "Я получил: " + (message.text or "<no text>"))
