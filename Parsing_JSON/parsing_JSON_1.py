
# Используйте полученный по ссылке 'https://parsinger.ru/downloads/get_json/res.json'
# JSON, чтобы посчитать количество товара в каждой категории.
#
# На вход ожидается словарь {'watch': N, 'mobile': N, 'mouse': N, 'hdd': N, 'headphones': N},
# где N - это общее количество товаров
# Количество вы найдёте в каждой карточке товара.
import requests

url = 'https://parsinger.ru/downloads/get_json/res.json'

response = requests.get(url).json()
caty = set([i['categories'] for i in response])
dct = dict(zip(caty, [0] * len(caty)))
for item in response:
    if item['categories'] in dct:
        dct[item['categories']] += int(item['count'])
print(dct)


