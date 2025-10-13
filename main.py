import telebot
from flask import Flask, request
import os

TOKEN = "8357091966:AAE_bsrgQAvwjb410w3vk7lLd2Dq6rxCheU"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive!"

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
    bot.process_new_updates([update])
    return "OK", 200

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! 🌿 Я философский бот. Каждый день — новая мудрость!")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, "🧠 Мудрость: философ ищет смысл, а не ответы.")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    bot.remove_webhook()
    bot.set_webhook(url=f'https://philosoph-quote-bot.onrender.com/{TOKEN}')
    app.run(host='0.0.0.0', port=port)
