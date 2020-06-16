true = True
false = False

array = {"ok": true,
         "result" : [
             {"update_id": 744894717,
              "message": {"message_id": 3,
                          "from": {"id": 381528184,
                                   "is_bot": false,
                                   "first_name": "Alexandr",
                                   "last_name": "Ivanov",
                                   "language_code": "ru-RU"},
                          "chat": {"id": 381528184,
                                   "first_name": "Alexandr",
                                   "last_name": "Ivanov",
                                   "type": "private"},
                          "date": 1520456317,
                          "text":"/start",
                          "entities": [{"offset":0,
                                       "length": 6,
                                        "type": "bot_command"}]}},
             {"update_id": 744894718,
              "message": {"message_id": 4,
                          "from":{"id": 381528184,
                                  "is_bot":false,
                                  "first_name": "Alexandr",
                                  "last_name":"Ivanov",
                                  "language_code":"ru-RU"},
                          "chat": {"id":381528184,
                                   "first_name": "Alexandr",
                                   "last_name": "Ivanov",
                                   "type": "private"},
                          "date": 1520456322,
                          "text": "\u041f\u0440\u0438\u0432\u0435\u0442"}}]}

def funfun(array):
    for key, value in array.items():
        if key == 'result':
            print('%s:' % key)
            for element in value:
                for key, value in element.items():
                    if type(value) == dict:
                        print(' ', key + ':')
                        for i, k in value.items():
                            if type(k) == dict:
                                print('    %s:' % i)
                                for key, value in k.items():
                                    print('      %s: %s' % (key, value))
                            else:
                                print('    %s: %s' % (i, k))
                    else:
                        print('  %s: %s' % (key, value))
        else:
            print('%s: %s' % (key, value))

funfun(array)