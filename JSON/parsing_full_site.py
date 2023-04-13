import json
import requests
from bs4 import BeautifulSoup

result = []


def make_soup(url, encoding='utf-8', parser_type='lxml'):
    response = requests.get(url=url)
    response.encoding = encoding
    soup = BeautifulSoup(response.text, parser_type)
    return soup


schema = 'https://parsinger.ru/html/'
url_start = 'https://parsinger.ru/html/index1_page_1.html'

soup = make_soup(url_start)

pagen = [int(i.text) for i in soup.find('div', class_='pagen').find_all('a')[-1]]
categories = [i['id'] for i in soup.find('div', class_='nav_menu').find_all('div')]

for p in range(pagen.pop() + 1):
    for num in range(1, 33):
        url = f'{schema + categories[p]}/{p + 1}/{p + 1}_{num}.html'
        soup = make_soup(url)
        name = [n.text.strip() for n in soup.find('p')]
        article = [a.text.split(': ') for a in soup.find_all('p', class_='article')]
        description = [d.text.strip().split(': ') for d in soup.find_all('li')]
        price = [p.text for p in soup.findAll('span')]

        for name, article in zip(name, article):
            result.append({

                'Категория': categories[p],
                'Название': name,
                article[0]: article[1],
                'Описание': {
                    description[0][0]: description[0][1],
                    description[1][0]: description[1][1],
                    description[2][0]: description[2][1],
                    description[3][0]: description[3][1],
                    description[4][0]: description[4][1],
                    description[5][0]: description[5][1],
                    description[6][0]: description[6][1],
                    description[7][0]: description[7][1]
                },
                'В наличии': price[0].split(':')[1],
                'Цена': price[1],
                'Старая цена': price[2],
                'Сайт': url
            })

with open('result.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, indent=4, ensure_ascii=False)
print('Файл result создан')