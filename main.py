import telebot
from flask import Flask
import threading, os

TOKEN = "8357091966:AAE_bsrgQAvwjb410w3vk7lLd2Dq6rxCheU"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive!"

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! 🌿 Я философский бот. Каждый день — новая мудрость!")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, "🧠 Мудрость: философ ищет смысл, а не ответы.")

def run_flask():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

def run_bot():
    bot.polling(none_stop=True, interval=0, timeout=30)
