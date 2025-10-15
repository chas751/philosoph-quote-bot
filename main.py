from flask import Flask, request
import requests
import logging

TOKEN = "8228885470:AAFxS7h1Y5bYxSyjhAVG7FIahdSaJCoESBs"
API_URL = f"https://api.telegram.org/bot{TOKEN}"

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/', methods=['POST'])
def webhook():
    update = request.get_json()
    logging.info(f"Incoming raw update: {update}")

    if 'message' in update:
        chat_id = update['message']['chat']['id']
        text = update['message'].get('text', '')

        if text == '/start':
            send_message(chat_id, "Привет! 👋 Я философский бот. Каждый день — новая мудрость.")
        else:
            send_message(chat_id, f"Ты написал: {text}")

    return 'OK', 200

def send_message(chat_id, text):
    requests.post(f"{API_URL}/sendMessage", json={'chat_id': chat_id, 'text': text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
