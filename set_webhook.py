import requests

TOKEN = "8228885470:AAFxS7h1Y5bYxSyjhAVG7FIahdSaJCoESBs"
WEBHOOK_URL = "https://philosoph-quote-bot.onrender.com"

set_webhook = f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={WEBHOOK_URL}"
response = requests.get(set_webhook)
print(response.json())
