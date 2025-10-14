import telebot
from flask import Flask, request

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)


import os
TOKEN = TOKEN = "8357091966:AAGdvUQnHejEjJ9B5RG69tNad9bVt7G-_1M"
@app.route('/')
def home():
    return "Bot is alive!"

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
    bot.process_new_updates([update])
