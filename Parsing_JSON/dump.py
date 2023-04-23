import requests
from bs4 import BeautifulSoup
import json
res = 0
for i in range(1, 33):
    url = f'https://parsinger.ru/html/headphones/5/5_{i}.html'
    responce = requests.get(url=url)
    responce.encoding = 'utf-8'
    soup = BeautifulSoup(responce.text, 'lxml')
    summa = [int(i.split(':')[1]) for i in soup.find('span', id='in_stock')]

    for s in summa:
        res += int(s)



with open('res.json', 'w', encoding='utf-8') as file:
    json.dump(res, file, indent=4, ensure_ascii=False)