import telebot
from flask import Flask, request

# 🔑 Твой токен
TOKEN = "8357091966:AAGdvUQnHejEjJ9B5RG69tNad9bVt7G-_1M"

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Главный маршрут — Telegram сюда шлёт обновления
@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        update = request.get_json()
        bot.process_new_updates([telebot.types.Update.de_json(update)])
        return '', 200
    else:
        return 'Bot is running!', 200


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Привет! 🤖 Бот работает!")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
