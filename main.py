import telebot
from flask import Flask, request

TOKEN = "8357091966:AAGdvUQnHejEjJ9B5RG69tNad9bVt7G-_1M"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        json_str = request.get_data().decode('UTF-8')
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
        return '', 200
    else:
        return 'Bot is alive!', 200

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "✅ Привет, я живой! Всё работает отлично.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
