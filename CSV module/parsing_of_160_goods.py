from bs4 import BeautifulSoup
import lxml
import requests
import csv
import time

start = time.time()

with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Наименование', 'Артикул', 'Бренд', 'Модель',
                     'Наличие', 'Цена', 'Старая цена', 'Ссылка на карточку с товаром'
                     ])

    categories = {1: 'watch', 2: 'mobile', 3: 'mouse', 4: 'hdd', 5: 'headphones'}
    for caty in range(5):
        for num in range(32):
            url = f'https://parsinger.ru/html/{categories[caty + 1]}/{caty + 1}/{caty + 1}_{num + 1}.html'
            response = requests.get(url=url)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'lxml')
            name = soup.find('p', id='p_header').text
            article = soup.find('p', class_='article').text.split(': ')[1]
            description = [d.text.split(': ')[1] for d in soup.findAll('li')]
            in_stock = soup.find('span', id='in_stock').text.split(': ')[1]
            price = [p.text.split(' ')[0] for p in soup.findAll('span')]
            link = url
# если у вас есть идея как спарсить через list comprehension 'div' class_='description' ,
# и вывести как-то по другому напишите пожалуйста)
            writer.writerow([name, article, description[0], description[1],
                             in_stock, price[1], price[2], link])

print('Ваш файл csv готов')

end = time.time() - start
print(end)
