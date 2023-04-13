from bs4 import BeautifulSoup
import requests
import json


def make_soup(url, encoding='utf-8', parser_type='lxml'):
    response = requests.get(url=url)
    response.encoding = encoding
    soup = BeautifulSoup(response.text, parser_type)
    return (soup)


url_start = 'https://parsinger.ru/html/index1_page_1.html'
schema = 'https://parsinger.ru/html/'

result_json = []

soup = make_soup(url_start)
categories = [link['href'] for link in soup.find('div', class_='nav_menu').find_all('a')]
cat = [x['id'] for x in soup.find('div', class_='nav_menu').find_all('div')]

menu = dict()

for i in range(len(categories)):
    menu[categories[i]] = cat[i]

for category in categories:
    pagen = list()

    category_url = schema + category
    soup = make_soup(category_url)
    pagen.extend([link['href'] for link in soup.find('div', class_='pagen').find_all('a')])

    for p in pagen:
        cards_urls = list()
        url = schema + p
        soup = make_soup(url)
        cards_urls.extend([schema + x['href'] for x in soup.find_all('a', class_='name_item')])

        for card in cards_urls:
            soup = make_soup(card)
            name = soup.find('p', id='p_header').text.strip()
            articul = soup.find('p', class_='article').text.split(":")[-1].strip()
            description = [x.text.strip() for x in soup.find('ul', id='description').find_all('li')]
            in_stock = soup.find('span', id="in_stock").text.split(":")[-1].strip()
            price = soup.find('span', id='price').text.strip()
            old_price = soup.find('span', id='old_price').text.strip()

            result_json.append({
                'categories': menu[category],
                'name': name,
                'article': articul,
                'descritption': {x.split(":")[0].strip(): x.split(":")[1].strip() for x in description},
                'count': in_stock,
                'price': price,
                'old_price': old_price,
                'link': card

            })

with open('res.json', 'w', encoding='utf-8') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)

print("Файл загружен. Записей", len(result_json))