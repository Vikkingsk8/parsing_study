import requests
from bs4 import BeautifulSoup
import json


response = requests.get('https://parsinger.ru/html/index5_page_1.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
pagen = [int(x.text) for x in soup.find('div', class_='pagen').find_all('a')][-1]
result_json = []
print(pagen)
link_all = []
for i in range(1, pagen + 1):
    url = f'https://parsinger.ru/html/index5_page_{i}.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    link = soup.find_all('a', class_='name_item')
    for x in link:
        link_all.append(f"https://parsinger.ru/html/{x['href']}")
        print(link)
# for url in tqdm(link_all):
#     response = requests.get(url=url)
#     response.encoding = 'utf-8'
#     soup = BeautifulSoup(response.text, 'lxml')
#
#     name = [x.text.strip() for x in soup.find_all('p', id='p_header')]
#     article = [x.text.split(':')[1].strip() for x in soup.find_all('p', class_='article')]
#     description = [x.text.strip().split('\n') for x in soup.find_all('ul', id='description')]
#     in_stock = [x.text.split(':')[1].strip() for x in soup.find_all('span', id='in_stock')]
#     price = [x.text for x in soup.find_all('span', id='price')]
#     old_price = [x.text.strip() for x in soup.find_all('span', id='old_price')]
#     url = url
#
#     for list_item, price_item, name, article, in_stock, old_price, link in zip(description, price, name, article,
#                                                                                in_stock, old_price, link):
#         result_json.append({
#             'name': name,
#             'article': article,
#             'description': {
#                 'brand': [x.split(':')[1].strip() for x in list_item][0],
#                 'model': [x.split(':')[1].strip() for x in list_item][1],
#                 'type': [x.split(':')[1].strip() for x in list_item][2],
#                 'frequency': [x.split(':')[1].strip() for x in list_item][3],
#                 'microphone': [x.split(':')[1].strip() for x in list_item][4],
#                 'wire_length': [x.split(':')[1].strip() for x in list_item][5],
#                 'connect': [x.split(':')[1].strip() for x in list_item][6],
#                 'unique': [x.split(':')[1].strip() for x in list_item][7]
#             },
#             'in_stock': in_stock,
#             'price': price_item,
#             'old_price': old_price,
#             'link': url
#         })
#
#     with open('finish1.json', 'w', encoding='utf-8') as file:
#         json.dump(result_json, file, indent=4, ensure_ascii=False)
#
# print('Файл finish1.json создан')
