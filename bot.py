import telebot
import time
import configuration
import api_condensates


bot = telebot.TeleBot(configuration.token)







#
#
# text = ''
# for parameter, data in data_condensates.items():
#     if parameter == 'Наименование':
#         text += '%s\n' % data
#     else:
#         text += '%s: %s\n' % (parameter, data)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    global text
    if message.text == 'begin':
        bot.send_message(message.chat.id, text)
    else:
        bot.send_message(message.chat.id, 'error')


old_data = []
upd = bot.get_updates()
last_upd = upd[-1]

while True:
    print('hello')
    new_data = api_condensates.main()
    for condensate in new_data:
        if condensate in old_data:
            continue
        else:
            old_data.append(condensate)
            global text
            text = ''
            for i, k in condensate.items():
                text += '%s: %s\n' % (i, k)
            time.sleep(3)
            handle_text(last_upd.message)

    time.sleep(5)

# bot.polling(none_stop=True, interval=0)






