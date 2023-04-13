from bs4 import BeautifulSoup
import requests
import json

result_json = []

url = 'https://parsinger.ru/html/index3_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
shema = 'https://parsinger.ru/html/'
pages = [f"{shema}{page['href']}" for page in soup.find('div', class_='pagen').find_all('a')]
print(pages)
# for page in pages:
#     url = page
#     response = requests.get(url=url)
#     response.encoding = 'utf-8'
#     soup = BeautifulSoup(response.text, 'lxml')
#     tovary = [f"{shema}{link['href']}" for link in soup.find('div', class_='item_card').find_all('a', {'class': 'name_item'})]
#
#     for tovar in tovary:
#         url = tovar
#         response = requests.get(url=url)
#         response.encoding = 'utf-8'
#         soup = BeautifulSoup(response.text, 'lxml')
#
#         name = soup.find('p', id='p_header').text
#         article = soup.find('p', class_='article').text.split(': ')
#         in_stock = soup.find('span', id='in_stock').text.split(': ')
#         price = soup.find('span', id='price').text
#         old_price = soup.find('span', id='old_price').text
#
#         description = [descr.text.split(': ') for descr in soup.find_all('li')]
#
#         result_json.append({
#             "Категория": "Мышь",
#             "Название": name,
#             article[0]: article[1],
#             "Описание": {
#                 description[0][0]: description[0][1],
#                 description[1][0]: description[1][1],
#                 description[2][0]: description[2][1],
#                 description[3][0]: description[3][1],
#                 description[4][0]: description[4][1],
#                 description[5][0]: description[5][1],
#                 description[6][0]: description[6][1],
#                 description[7][0]: description[7][1]
#             },
#             in_stock[0]: in_stock[1],
#             "Цена": price,
#             "Старая цена": old_price,
#             "Ссылка": url
#         })
#
# with open('res.json', 'w', encoding='utf-8') as file:
#     json.dump(result_json, file, indent=4, ensure_ascii=False)