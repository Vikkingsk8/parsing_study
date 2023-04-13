from bs4 import BeautifulSoup
import requests
import json


def make_soup(url, encoding='utf-8', parser_type='lxml'):
    response = requests.get(url=url)
    response.encoding = encoding
    soup = BeautifulSoup(response.text, parser_type)
    return (soup)


url_start = 'https://parsinger.ru/html/index3_page_1.html'
schema = 'https://parsinger.ru/html/'

result_json = []
cards_urls = list()

soup = make_soup(url_start)
pagen = [link['href'] for link in soup.find('div', class_='pagen').find_all('a')]
print(pagen)
for p in pagen:
    url = schema + p
    soup = make_soup(url)
    cards_urls.extend([schema + x['href'] for x in soup.find_all('a', class_='name_item')])
print(cards_urls)
for card in cards_urls:
    soup = make_soup(card)
    name = soup.find('p', id='p_header').text
    description = [x.text for x in soup.find('ul', id='description').find_all('li')]
    in_stock = soup.find('span', id="in_stock").text
    price = soup.find('span', id='price').text
    old_price = soup.find('span', id='old_price').text

    result_json.append({
        'Название': name,
        description[0].split(":")[0]: description[0].split(":")[1],
        description[1].split(":")[0]: description[1].split(":")[1],
        description[2].split(":")[0]: description[2].split(":")[1],
        description[3].split(":")[0]: description[3].split(":")[1],
        description[4].split(":")[0]: description[4].split(":")[1],
        description[5].split(":")[0]: description[5].split(":")[1],
        description[6].split(":")[0]: description[6].split(":")[1],
        description[7].split(":")[0]: description[7].split(":")[1],
        'Цена': price,
        'Старая цена': old_price

    })

with open('res.json', 'w', encoding='utf-8') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)

print("Файл загружен. Записей", len(result_json))