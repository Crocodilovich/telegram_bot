import requests
import misc
import yobit
import time


TOKEN = misc.TOKEN
URL = 'https://api.telegram.org/bot' + TOKEN + '/'


global last_update_id
last_update_id = 0


def get_updates():
    """Получение пакета обновлений"""
    url = URL + 'getUpdates'
    response = requests.get(url)

    return response.json()


def get_message():
    """Получение сообщения от пользователя"""
    data = get_updates()

    current_update_id = data['result'][-1]['update_id']
    id_user = data['result'][-1]['message']['chat']['id']
    message_text = data['result'][-1]['message']['text']

    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id
        user_message = {
            'id_user': id_user,
            'message_text': message_text
        }
        return user_message
    return None


def send_message(chat_id, message_text='Enter your message...'):
    """Отправка сообщения пользователю"""
    url = '{}sendMessage?chat_id={}&text={}'.format(URL, chat_id, message_text)
    requests.get(url)


def main():


    while True:
        answer = get_message()

        if answer != None:
            id_user = answer['id_user']
            text = answer['message_text']

            if text == '/btc':
                send_message(id_user, yobit.get_btc())
        else:
            continue
        time.sleep(3)


if __name__ == '__main__':
    main()