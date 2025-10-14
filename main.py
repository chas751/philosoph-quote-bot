import telebot
from flask import Flask, request

# 🔑 ВСТАВЛЯЕМ ТОКЕН СЮДА:
TOKEN = "8357091966:AAGdvUQnHejEjJ9B5RG69tNad9bVt7G-_1M"

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive!", 200

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return 'OK', 200

bot.remove_webhook()
bot.set_webhook(url=f'https://philosoph-quote-bot.onrender.com/{TOKEN}')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, Стас! Я живой бот ✌️")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
