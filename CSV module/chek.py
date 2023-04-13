import csv
import requests
from bs4 import BeautifulSoup

'''Доброго времени суток, уважаемый (ая) проверяющий!
Не суди строго =Р!'''

url = 'https://parsinger.ru/html/watch/1/'

# начинаем работу в менеджере контекста
with open('result.csv', 'a', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')  # создаем объект для записи данных

    # записываем строку с названиями столбцов в csv-документе
    writer.writerow(['Наименование',
                     'Артикул',
                     'Бренд',
                     'Модель',
                     'Тип',
                     'Технология экрана',
                     'Материал корпуса',
                     'Материал браслета',
                     'Размер',
                     'Сайт производителя',
                     'Наличие',
                     'Цена',
                     'Старая цена',
                     'Ссылка на карточку с товаром'
                     ])

    # используем цикл for для пагинации
    for item in range(1, 33):
        response = requests.get(url=f'{url}1_{item}.html')  # цикличный запрос к url
        response.encoding = 'utf-8'  # устанавливаем кодировку для полученного ответа
        soup = BeautifulSoup(response.text, 'lxml')  # считываем html-код для странички с часами

        name = soup.select('div.description p#p_header')[0].text  # название часов
        article = soup.select('div.description p.article')[0].text.split(':')[1].strip()  # артикул часов
        description = map(lambda x: x.split(':')[1].strip(),  # парсим блок с елементами описания часов
                          (tag.text.strip() for tag in
                           soup.find('ul', id='description').find_all('li')))
        in_stock = soup.select('div.description span')[0].text.split(':')[1].strip()  # количество часов в наличии
        cost = soup.select('span#price')[0].text  # текущая стоимость часов
        old_cost = soup.select('span#old_price')[0].text  # первоначальная стоимость часов
        link = f'{url}1_{item}.html'  # ссылка на товар

        writer.writerow([name, article, *description, in_stock, cost, old_cost, link])  # записываем полученные данные
