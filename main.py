import telebot
import time
import random
import threading

# 🔑 Твой токен
TOKEN = "8357091966:AAE_bsrgQAvwjb410w3vk7lLd2Dq6rxCheU"
bot = telebot.TeleBot(TOKEN)

# 📜 Список цитат
quotes = [
    '"Познай самого себя." — Сократ',
    '"Я мыслю, следовательно, я существую." — Декарт',
    '"Человек есть то, что он делает." — Сартр',
    '"Мужество — это знать, чего не стоит бояться." — Платон',
    '"Мудрый человек не говорит всё, что думает." — Аристотель',
]

# 🕊️ Оформление сообщения
def format_quote(quote):
    return f"""📜 *Мудрость дня*\n
_{quote}_

━━━━━━━━━━━━━━━━━━━
💬 Поддержать проект:
💳 ВТБ: 2200 2460 3013 9912
"""

# 💫 Автоматическая отправка цитаты каждые 2 часа
def send_quote_periodically():
    while True:
        quote = random.choice(quotes)
        message = format_quote(quote)
        bot.send_message("@daily_philosoph", message, parse_mode="Markdown")
        time.sleep(7200)  # 2 часа = 7200 секунд

# 🧩 Запуск фонового потока
threading.Thread(target=send_quote_periodically, daemon=True).start()

# 💬 Возможность ручной публикации
@bot.message_handler(commands=['quote'])
def send_quote(message):
    quote = random.choice(quotes)
    formatted = format_quote(quote)
    bot.send_message(message.chat.id, formatted, parse_mode="Markdown")

# 🚀 Запуск
bot.polling(none_stop=True)

