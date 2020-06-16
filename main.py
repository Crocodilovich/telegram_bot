from flask import Flask
from flask import request
from flask import jsonify
from flask_sslify import SSLify
import requests
import json
import re


app = Flask(__name__)
sslify = SSLify(app)


TOKEN = '554986507:AAEjnVUlIskTERPpVg_sqs_3Eg6bf4d21jI'
URL = 'https://api.telegram.org/bot%s/' % TOKEN


def write_json(data, file_name='answer.json'):
    """Обработка данных"""
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def send_message(chat_id, text='text-text-text'):
    """Отправка сообщения"""
    url = '%ssendMessage?chat_id=%s&text=%s' % (URL, chat_id, text)
    answer = {'chat_id': chat_id,
              'text': text}
    response = requests.post(url, json=answer)

    return response.json()


def parse_text(text):
    pattern = r'/\w+'
    crypto = re.search(pattern, text).group()

    return crypto[1:]


def get_price(crypto):
    url = 'https://api.coinmarketcap.com/v1/ticker/{}'.format(crypto)
    response = requests.get(url).json()
    price = response[-1]['price_usd']
    # write_json(response.json(), file_name='price.json')
    return price


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        response = request.get_json()
        chat_id = response['message']['chat']['id']
        message = response['message']['text']

        pattern = r'/\w+'

        if re.search(pattern, message):
            price = get_price(parse_text(message))
            send_message(chat_id, price)

        # write_json(response)
        return jsonify(response)

    return '<h1>Bot welcomes you<h1>'


if __name__ == '__main__':
    app.run()
