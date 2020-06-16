import requests

def get_btc():
    url = 'http://yobit.net/api/2/btc_usd/ticker'
    response = requests.get(url).json()
    price = (response['ticker']['last'])

    return '%s usd' % price

print(get_btc())