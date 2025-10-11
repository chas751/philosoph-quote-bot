import telebot
import random
import time

TOKEN = "сюда_вставь_свой_бот_токен"  # вставь свой токен
bot = telebot.TeleBot(TOKEN)

# Список философских цитат
quotes = [
    "📜 «Познай самого себя.» — Сократ",
    "📜 «Мы становимся тем, о чём думаем.» — Будда",
    "📜 «Счастье зависит от нас самих.» — Аристотель",
    "📜 «Мудрость — это знание того, что ты ничего не знаешь.» — Сократ",
    "📜 «Не тот велик, кто никогда не падал, а тот, кто поднимается каждый раз, когда падает.» — Конфуций",
]

donate_message = """
💫 Поддержи проект философских цитат:

💰 TRX (USDT): `TErjzxxbTg1uvhEDBzpnvDr2p3g1RRw5Pd`

🙏 Благодарю за помощь и интерес к мудрости!
"""

# Переменная для счёта сообщений
message_count = 0

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "🧘‍♂️ Добро пожаловать в «Мудрость дня»!\nКаждый день — новая мысль великих философов.\n\nНапиши /quote, чтобы получить цитату.",
    )

@bot.message_handler(commands=["quote"])
def send_quote(message):
    global message_count
    quote = random.choice(quotes)
    message_count += 1

    bot.send_message(message.chat.id, quote)

    # Каждые 5 сообщений добавляем реквизиты
    if message_count % 5 == 0:
        time.sleep(1)
        bot.send_message(message.chat.id, donate_message, parse_mode="Markdown")

print("🤖 Бот запущен успешно!")
bot.polling(none_stop=True)
