# import json
# import requests
# from bs4 import BeautifulSoup
#
# result_json = []
# for i1 in range(1, 6):
#     for i2 in range(1,5):
#         url = f'https://parsinger.ru/html/index{i1}_page_{i2}.html'
#         response = requests.get(url)
#         response.encoding = 'utf-8'
#         soup = BeautifulSoup(response.text, 'html.parser')
#         items = soup.find_all('div', class_='item')
#         for item in items:
#             dict = {}
#             name = item.find('a', class_='name_item').text.strip()
#             dict['Имя'] = name
#             description = item.find_all('li')
#             for descr in description:
#                 d = descr.text.split(':')
#                 dict[d[0].strip()] = d[1].strip()
#             dict['Цена'] = item.find('p', class_='price').text.strip()
#             result_json.append(dict)
#
# with open('test2.json', 'w', encoding='utf-8') as file:
#     json.dump(result_json, file, indent=4, ensure_ascii=False)
import requests

from bs4 import BeautifulSoup

import json
#
# url = "https://parsinger.ru/html/index5_page_1.html"
#
# catalog_items = []
#
#
# def cook_soup(url):
#     res = requests.get(url=url)
#
#     res.encoding = "utf-8"
#
#     return BeautifulSoup(res.text, "lxml")
#
#
# all_catalog = [f"https://parsinger.ru/html/" + i["href"] for i in
#                cook_soup(url).find("div", class_="nav_menu").find_all("a")]
#
# for url in all_catalog:
#
#     pagen = [f"https://parsinger.ru/html/" + i["href"] for i in
#              cook_soup(url).find("div", class_="pagen").find_all("a")]
#
#     for url in pagen:
#
#         soup = cook_soup(url)
#
#         name_item = [i.text.strip() for i in soup.find_all("a", class_="name_item")]
#
#         description = [x.text.strip().split('\n') for x in soup.find_all('div', class_='description')]
#
#         price = [x.text for x in soup.find_all('p', class_='price')]
#
#         for desc, name, pr in zip(description, name_item, price):
#             catalog_items.append({
#
#                 "имя товара": name,
#
#                 desc[0].split(":")[0]: desc[0].split(":")[1],
#
#                 desc[1].split(":")[0]: desc[1].split(":")[1],
#
#                 desc[2].split(":")[0]: desc[2].split(":")[1],
#
#                 desc[3].split(":")[0]: desc[3].split(":")[1],
#
#                 "цена": pr
#
#             })
#
# with open("reshed.json", "w", encoding="utf-8") as file:
#     json.dump(catalog_items, file, indent=4, ensure_ascii=False)
import requests
from bs4 import BeautifulSoup

response = requests.get('http://parsinger.ru/html/watch/1/1_1.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
description = soup.find('ul', id='description').find_all('li')

for li in description:
    print(li['id'])