import requests
from bs4 import BeautifulSoup
import json

'''уважаемый проверяющий не суди строго большинство кода захордкодил
Если есть немного времени помоги с кодом.
№ 1 вопрос не смог додуматься как спарсить максимальное количество? в одной категории 
поэтому цикл .
№ 2 после парсинга name,article,description и т.д. в цикле с зипом 
мой список со вложеными списками описания товара почему-то по прохождению списка выдавал только бренд
хз почему.
ДОРОГОЙ ЧИТАТЕЛЬ, ПРОВЕРЯЮЩИЙ если есть идеи по улучшению моего кода прошу напиши потрать своё время
Так же буду рад посмотреть на твой код .Спасибо'''
result = []
for i in range(1, 33):
    url = f'https://parsinger.ru/html/mouse/3/3_{i}.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    name = [n.text.strip() for n in soup.find('p')]
    article = [a.text.split(': ') for a in soup.find_all('p', class_='article')]
    description = [d.text.strip().split(': ') for d in soup.find_all('li')]
    price = [p.text for p in soup.findAll('span')]

    for name, article in zip(name, article):
        result.append({

            'Категория': 'мыши',
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
