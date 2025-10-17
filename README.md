# philosoph-quote-bot

Простой Telegram-бот, присылающий философские цитаты.

## Состав проекта
- `bot.py` — основной код бота (использует aiogram).
- `requirements.txt` — зависимости для установки (`pip install -r requirements.txt`).
- `Procfile` — команда запуска для Render (worker).
- `runtime.txt` — версия Python для Render (python-3.11.8).
- `README.md` — этот файл.

## Настройка перед деплоем
1. Создай репозиторий на GitHub и загрузите все файлы (в корень репозитория).
2. На Render (https://render.com) создай **Web Service** или **Background Worker**:
   - Если используешь **Render Free**, выбери **Web Service** и в `bot.py` оставлен `worker` — но лучше выбрать **Background Worker** (если доступно).
3. Добавь переменную окружения в Render (Dashboard → Environment):
   - Key: `TELEGRAM_TOKEN`
   - Value: `<твой_токен_от_BotFather>`

## Локальный запуск (тест)
1. Установи зависимости:
```bash
pip install -r requirements.txt
```
2. Установи переменную окружения локально (пример для Linux/macOS):
```bash
export TELEGRAM_TOKEN="твой_токен"
python bot.py
```
Для Windows (PowerShell):
```powershell
$env:TELEGRAM_TOKEN="твой_токен"
python bot.py
```

## Деплой на Render (кратко)
1. Создай новый сервис → выбери репозиторий и ветку `main`.
2. Build Command: `pip install -r requirements.txt`
3. Start Command: оставь пустым (Render использует Procfile) или запиши `python bot.py`.
4. В Procfile указан:
```
worker: python bot.py
```
5. Добавь `TELEGRAM_TOKEN` в Environment на Render.
6. Нажми Deploy.

## Примечания
- Не выкладывай реальный токен в публичный репозиторий. Используй переменные окружения на Render.
- Бесплатные Render инстансы "спят" при простое — первая реакция может занять ~50 секунд.
- Если будут ошибки во время `pip install` — пришлите лог, помогу исправить версии зависимостей.
