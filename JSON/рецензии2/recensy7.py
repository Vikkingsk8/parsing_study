from bs4 import BeautifulSoup
import requests
import json

shema = 'https://parsinger.ru/html/'


def get_descr():
    # получение ссылок
    def get_url(url):
        response = requests.get(url=url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        return soup

    # получение категорий
    def get_categories():
        star_url = 'https://parsinger.ru/html/index1_page_1.html'
        soup = get_url(star_url)
        categories = [f"{shema}{link['href']}" for link in soup.find('div', class_='nav_menu').find_all('a')]
        return categories

    # получение страниц в каждой категории
    def get_pages():
        categories = get_categories()
        pages = []
        for categori in categories:
            soup = get_url(categori)
            link = [f"{shema}{page['href']}" for page in soup.find('div', class_='pagen').find_all('a')]
            pages.append(link)
        return pages

    # получение ссылок на карточки товара
    def get_tovary():
        pages = get_pages()
        tovary = []
        for i in pages:
            for j in i:
                soup = get_url(j)
                tovar = [f"{shema}{link['href']}" for link in soup.find_all('a', {'class': 'name_item'})]
                tovary.append(tovar)
        return tovary

    # получение описание словаря
    def get_description():
        tovar = get_tovary()
        result_json = []
        for i in tovar:
            for j in i:
                soup = get_url(j)
                name = soup.find('p', id='p_header').text
                article = soup.find('p', class_='article').text.split(': ')
                in_stock = soup.find('span', id='in_stock').text.split(': ')
                price = soup.find('span', id='price').text
                old_price = soup.find('span', id='old_price').text
                description = [descr.text.split(': ') for descr in soup.find('ul', id='description').find_all('li')]

                result_json.append({
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
                    in_stock[0]: in_stock[1],
                    'Цена': price,
                    'Старая цена': old_price,
                    'Ссылка': j
                })
        return result_json

    return get_description()


with open('res.json', 'w', encoding='utf-8') as file:
    json.dump(get_descr(), file, indent=4, ensure_ascii=False)