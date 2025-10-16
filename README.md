# philosoph-quote-bot 🤖

Философский Telegram-бот, присылающий мудрые цитаты.

## Команды
- `/start` — приветствие
- `/quote` — случайная цитата

## Локальный запуск
1. Создай файл `.env` и добавь:
   ```
   TOKEN=твой_токен
   ```
2. Установи зависимости:
   ```
   pip install -r requirements.txt
   ```
3. Запусти:
   ```
   python bot.py
   ```

## Render деплой
- Добавь переменную окружения `TOKEN`
- Укажи Python 3.10.13 (runtime.txt)
- Procfile: `worker: python bot.py`
