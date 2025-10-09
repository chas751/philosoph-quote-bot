import telebot
import random
import time
from datetime import datetime, timedelta

TOKEN = "8357091966:AAE_bsrgQAvwjb410w3vk7lLd2Dq6rxCheU"
CHANNEL_ID = "@daily_philosoph"
bot = telebot.TeleBot(TOKEN)

quotes = [
    "«Познай самого себя.» — Сократ",
    "«Мы становимся тем, о чём думаем.» — Будда",
    "«Счастье — это не цель, а путь.» — Конфуций",
    "«Человек есть то, что он делает.» — Жан-Поль Сартр",
    "«Свобода — осознанная необходимость.» — Гегель",
    "«Думай о прекрасном, и ты сам станешь прекрасным.» — Платон"
]

next_post_time = datetime.now()

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я бот «Мудрость философов каждый день». Каждые 2 часа я публикую цитаты в канале.")

@bot.message_handler(commands=['add'])
def add_quote(message):
    quote = message.text.replace("/add", "").strip()
    if quote:
        quotes.append(quote)
        bot.reply_to(message, "Цитата добавлена!")
    else:
        bot.reply_to(message, "Напиши цитату после команды /add")

def post_quote():
    global next_post_time
    if datetime.now() >= next_post_time:
        quote = random.choice(quotes)
        bot.send_message(CHANNEL_ID, f"📜 {quote}\n\n💳 Поддержать проект: 2200 2460 3013 9912 (ВТБ)")
        next_post_time = datetime.now() + timedelta(hours=2)

def main_loop():
    while True:
        post_quote()
        time.sleep(60)

if __name__ == "__main__":
    bot.polling(none_stop=True)
