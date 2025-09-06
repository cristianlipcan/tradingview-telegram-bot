from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = "7985772555:AAFxwAVWDmnihM_BZPpI8b8vso6bdS1jwCI"
CHAT_ID = "1024585490"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data.get('message', 'Semnal nou de la TradingView')
    
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, json=payload)
    
    return "ok", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
