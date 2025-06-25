from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return {"status": "alive", "message": "✅ Mithun's AutoChat Bot is Running!", "service": "telegram-auto-reply-bot"}

def run():
    app.run(host='0.0.0.0', port=5000)

def keep_alive():
    t = Thread(target=run)
    t.start()