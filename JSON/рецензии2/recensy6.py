from bs4 import BeautifulSoup, Tag
import requests
import json


def get_value(tag: Tag) -> str:
    return tag.text.split(':', maxsplit=1)[-1].strip()


def writer_json(js: list) -> None:
    with open('data.json', 'w', encoding='utf-8') as data:
        json.dump(js, data, indent=4, ensure_ascii=False)


def get_response(url: str) -> requests.Response:  # функция получения ответа от указанного url
    temp_response = requests.get(url)
    temp_response.encoding = 'utf-8'
    return temp_response


def get_pagen(soup: BeautifulSoup, schema: str = 'https://parsinger.ru/html/') -> list[requests.Response]:
    return [get_response(f"{schema}{tag['href']}")
            for tag in soup.find('div', class_='pagen').find_all('a', href=True)]


def get_items_info(tag_item: Tag) -> dict[str, str | dict]:
    info = {'name': tag_item.find('p', id='p_header').text.strip(),
            'article': get_value(tag_item.find('p', class_='article')),
            'description': {
                tag['id']: get_value(tag)
                for tag in tag_item.find('ul', id='description').find_all('li')
            },
            'count': get_value(tag_item.find('span', id='in_stock')),
            'price': tag_item.find('span', id='price').text.strip(),
            'old_price': tag_item.find('span', id='old_price').text.strip()}
    return info


def get_navigation_menu(soup: BeautifulSoup) -> list[tuple[requests.Response, str | list[str]]]:
    schema: str = 'https://parsinger.ru/html/'
    return [(get_response(f"{schema}{tag['href']}"), tag.next['id'])
            for tag in soup.find('div', class_='nav_menu').find_all('a', href=True)]


def get_links_cards(soup: BeautifulSoup, schema: str = 'https://parsinger.ru/html/'):
    return [f"{schema}{tag['href']}"
            for tag in soup.find_all('a', class_='name_item')]


response = get_response('https://parsinger.ru/html/index3_page_1.html')

main = BeautifulSoup(response.text, 'lxml')

result: list = []
for menu, categories in get_navigation_menu(soup=main):
    pages = get_pagen(soup=BeautifulSoup(menu.text, 'lxml'))
    for page in pages:
        items = get_links_cards(soup=BeautifulSoup(page.text, 'lxml'))
        for link_item in items:
            item = BeautifulSoup(get_response(link_item).text, 'lxml').find('div', class_='description')
            item_card = dict(categories=categories,
                             **get_items_info(item),
                             link=link_item)
            result.append(item_card)

writer_json(result)