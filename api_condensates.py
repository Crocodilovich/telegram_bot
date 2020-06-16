from bs4 import BeautifulSoup
import re
import requests


url = 'Ход торгов в Секции «Нефтепродукты»2.html'
TOKEN = '558244466:AAGgDFfosI-1sQBIMCgtpVr7Gua8UNjSaLQ'
URL = 'https://api.telegram.org/bot' + TOKEN + '/'


def get_html(url):
    """Получение html-страницы"""
    html = open(url, encoding='utf-8').read()

    return html


def get_id_condensates(html):
    """Получение всех id конденсаторов"""
    soup = BeautifulSoup(html, 'lxml')
    pattern = 'газовый'
    condensates = soup.find_all(text=re.compile(pattern))
    id_condensates = []
    for element in condensates:
        id_condensate = element.find_parent('tr').get('id')
        id_condensates.append(id_condensate)

    return id_condensates


def get_api_condensates(html, id_condensates):
    """Формирование API конденсаторов"""
    soup = BeautifulSoup(html, 'lxml')
    api_condensates = []

    for condensate in id_condensates:
        try:
            name_condensate = soup.find('tr', id=condensate).find('a').text
        except:
            name_condensate = '-'
        try:
            offer_price_condensate = soup.find('tr', id=condensate).find('span', class_='red').text
        except:
            offer_price_condensate = '-'
        try:
            offer_amount_condensate = soup.find('tr', id=condensate).find('span', class_='gray').text
        except:
            offer_amount_condensate = '-'
        try:
            demand_price_condensate = soup.find('tr', id=condensate).find('span', class_='green').text
        except:
            demand_price_condensate = '-'
        try:
            demand_amount_condensate = soup.find('tr', id=condensate).find('span', class_='green').parent.find('span', class_='gray').text
        except:
            demand_amount_condensate = '-'
        try:
            contracts_condensate = soup.find('tr', id=condensate).find('td', style='text-align: right;').next_sibling.next_sibling.text
            if contracts_condensate == '—':
                contracts_condensate = '-'

        except:
            contracts_condensate = '-'
        try:
            sum_contracts_condensate = soup.find('tr', id=condensate).find('td', style='text-align: right;').text
            new = ''
            for letter in sum_contracts_condensate:
                if letter.isalpha():
                    new += ' '
                elif letter.isdigit():
                    new += letter
                else:
                    new += ''
            sum_contracts_condensate = new.split()

            sum_ = sum_contracts_condensate[0]
            amount = sum_contracts_condensate[1]
        except:
            sum_ = '-'
            amount = '-'

        array_data = {'Наименование': name_condensate,
                      'Цена предложения': offer_price_condensate,
                      'Объем предложения': offer_amount_condensate,
                      'Цена спроса': demand_price_condensate,
                      'Объем спроса': demand_amount_condensate,
                      'Количество договоров': contracts_condensate,
                      'Сумма договоров': sum_,
                      'Объем договоров': amount}

        api_condensates.append(array_data)

    return api_condensates


def main():
    html = get_html(url)
    id_condensates = get_id_condensates(html)
    api_condensates = get_api_condensates(html, id_condensates)

    print(api_condensates[2]['Количество договоров'])
    print('—')

    return api_condensates

main()