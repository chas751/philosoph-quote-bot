import telebot
from flask import Flask, request
import os

TOKEN = 8357091966:AAGdvUQnHejEjJ9B5RG69tNad9bVt7G-_1M
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
