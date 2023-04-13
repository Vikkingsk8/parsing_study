import json
from bs4 import BeautifulSoup
import requests

response = requests.get(url='https://parsinger.ru/html/index1_page_1.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
pagen = [int(i.text) for i in soup.find('div', class_='pagen').find_all('a')[-1]]
category = [i.text for i in soup.find('div', class_='nav_menu').find_all('a')]
pagen = pagen.pop()
# print(pagen)
# print(len(category))

result = []
for caty in range(1, len(category) + 1):
    for p in range(1, pagen + 1):
        url = f'https://parsinger.ru/html/index{caty}_page_{p}.html'
        response = requests.get(url=url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        name = [n.text.strip() for n in soup.find_all('a', class_='name_item')]
        description = [d.text.strip().split('\n') for d in soup.find_all('div', class_='description')]
        price = [p.text for p in soup.find_all('p', class_='price')]
        print(description)
        # for list_item, price_item, name in zip(description, price, name):
        #     result.append({
        #         'Название': name,
        #         list_item[0].split()[0]: list_item[0].split(':')[1],
        #         list_item[1].split()[0]: list_item[1].split(':')[1],
        #         list_item[2].split()[0]: list_item[2].split(':')[1],
        #         list_item[3].split()[0]: list_item[3].split(':')[1],
        #         'Цена': price_item
        #
        #     })
        #
        #     with open('result.json', 'w', encoding='utf-8') as file:
        #         json.dump(result, file, indent=4, ensure_ascii=False)
