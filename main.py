import telebot
import random
import time
import threading

# Токен Telegram-бота
TOKEN = "8357091966:AAE_bsrgQAvwjb410w3vk7lLd2Dq6rxCheU"
bot = telebot.TeleBot(TOKEN)

# Список цитат (можно дополнять вручную)
quotes = [
    ("«Познай самого себя.»", "Сократ"),
    ("«Мы то, что мы постоянно делаем. Следовательно, совершенство — это не действие, а привычка.»", "Аристотель"),
    ("«Человек рожден свободным, но всюду он в цепях.»", "Жан-Жак Руссо"),
    ("«Тот, кто имеет 'зачем' жить, может вынести почти любое 'как'.»", "Фридрих Ницше"),
    ("«Не в силе Бог, а в правде.»", "Ф.М. Достоевский"),
    ("«Счастье — это не состояние, а путь.»", "Будда"),
    ("«Истинное богатство — это умение довольствоваться малым.»", "Платон")
]

CHANNEL_ID = "@daily_philosoph"  # Канал для публикации

# Обработка команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "🕊 Добро пожаловать в канал 'Мудрость философов каждый день'!\n\n"
                          "Бот публикует философские цитаты каждые 2 часа.\n"
                          "Вы также можете получить цитату вручную командой /цитата.")

# Команда для ручной публикации цитаты
@bot.message_handler(commands=['цитата'])
def send_quote(message):
    quote, author = random.choice(quotes)
    formatted = f"📜 *Мудрость философов каждый день* 🕊\n\n{quote}\n— _{author}_\n\n💬 #Философия #Мудрость\n💳 Поддержать проект: 2200 2460 3013 9912 (ВТБ)"
    bot.send_message(message.chat.id, formatted, parse_mode='Markdown')

# Фоновая публикация каждые 2 часа
def send_quote_periodically():
    while True:
        quote, author = random.choice(quotes)
        formatted = f"📜 *Мудрость философов каждый день* 🕊\n\n{quote}\n— _{author}_\n\n💬 #Философия #Мудрость\n💳 Поддержать проект: 2200 2460 3013 9912 (ВТБ)"
        try:
            bot.send_message(CHANNEL_ID, formatted, parse_mode='Markdown')
            print(f"✅ Опубликовано: {quote} — {author}")
        except Exception as e:
            print("⚠️ Ошибка при отправке:", e)
        time.sleep(7200)  # каждые 2 часа

# Запуск фонового потока
threading.Thread(target=send_quote_periodically, daemon=True).start()

print("✅ Бот запущен...")
bot.infinity_polling()

