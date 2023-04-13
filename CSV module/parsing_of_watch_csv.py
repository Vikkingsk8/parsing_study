from bs4 import BeautifulSoup
import requests
import csv
import lxml
import time

start = time.time()

with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Наименование', 'Артикул', 'Бренд', 'Модель', 'Тип',
                     'Технология экрана', 'Материал корпуса', 'Материал браслета',
                     'Размер', 'Сайт производителя', 'Наличие', 'Цена', 'Старая цена', 'Ссылка на карточку с товаром'
                     ])

    for num_goods in range(1, 33):
        url = f'https://parsinger.ru/html/watch/1/1_{num_goods}.html'
        response = requests.get(url=url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        name = soup.find('p', id='p_header').text
        article = soup.find('p', class_='article').text.split(': ')[1]
        brand = soup.find('li', id='brand').text.split(': ')[1]
        model = soup.find('li', id='model').text.split(': ')[1]
        type = soup.find('li', id='type').text.split(': ')[1]
        display = soup.find('li', id='display').text.split(': ')[1]
        material_frame = soup.find('li', id='material_frame').text.split(': ')[1]
        material_bracer = soup.find('li', id='material_bracer').text.split(': ')[1]
        size = soup.find('li', id='size').text.split(': ')[1]
        site = soup.find('li', id='site').text.split(': ')[1]
        in_stock = soup.find('span', id='in_stock').text.split(': ')[1]
        price = soup.find('span', id='price').text.split(' ')[0]
        old_price = soup.find('span', id='old_price').text.split(' ')[0]
        link = url

        writer.writerow([name, article, brand, model, type, display,
                         material_frame, material_bracer, size, site, in_stock, price, old_price,
                         link])

print('Файл res.csv создан')

end = time.time() - start
print(end)
