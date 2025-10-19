# daily_philosoph_bot (ready package)

Файлы внутри архива:
- bot.py — основной код бота
- requirements.txt — зависимости
- runtime.txt — версия Python для Render
- Procfile — команда запуска (web: python bot.py)
- .env — содержит BOT_TOKEN (включён по просьбе)

Инструкция для Render (кратко):
1. На Render создайте новый Web Service → Deploy from ZIP → загрузите этот zip.
2. В Build Command укажите: pip install -r requirements.txt
3. В Start Command можно оставить пустым (Render использует Procfile) или поставить: python bot.py
4. Рекомендуется в настройках Environment удалить файл .env и добавить ключ BOT_TOKEN в переменные среды Render (KEY=BOT_TOKEN, VALUE=<твой токен>), чтобы не хранить токен в репозитории публично.

Локально запуск:
1. python -m venv venv
2. source venv/bin/activate  # или venv\Scripts\activate on Windows
3. pip install -r requirements.txt
4. python bot.py