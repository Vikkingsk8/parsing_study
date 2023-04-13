import json
from bs4 import BeautifulSoup
import requests

# код для вычисления максимального количества страниц пагинации(если бы мы не знали сколько всего страниц)
# url = 'https://parsinger.ru/html/index1_page_1.html'
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# pagen = [int(link.text) for link in soup.find('div', class_='pagen').find_all('a')[-1]]
# pagen = pagen.pop()

result = []
for p in range(1, 5):
    url = f'https://parsinger.ru/html/index1_page_{p}.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    name = [n.text.strip() for n in soup.findAll('a', class_='name_item')]
    description = [d.text.strip().split('\n') for d in soup.findAll('div', class_='description')]
    price = [p.text for p in soup.findAll('p', class_='price')]

    for list_item, price_item, name in zip(description, price, name):
        result.append({
            'name': name,
            'brand': list_item[0].split(':')[1],
            'type': list_item[1].split(':')[1],
            'material': list_item[2].split(':')[1],
            'screen': list_item[3].split(':')[1],
            'price': price_item

        })

with open('result.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, indent=4, ensure_ascii=False)
