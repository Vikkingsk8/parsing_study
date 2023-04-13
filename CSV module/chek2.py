from bs4 import BeautifulSoup

import lxml, csv, requests

with open('file.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')

    writer.writerow(['Наименование', 'Артикул', 'Бренд', 'Модель', 'Наличие', 'Цена', 'Старая цена', 'Ссылка'])

    for n, i in enumerate(['watch', 'mobile', 'mouse', 'hdd', 'headphones'], 1):

        for j in range(1, 33):
            url = f'https://parsinger.ru/html/{i}/{n}/{n}_{j}.html'

            response = requests.get(url=url);
            response.encoding = 'utf-8'

            soup = BeautifulSoup(response.text, 'lxml').find('div', class_='item_card').find('div',
                                                                                             class_='description')

            writer.writerow([soup.find('p', id='p_header').text, soup.find('p', 'article').text.split(':')[-1].strip(),
                             *[i.text.split(':')[-1].strip() for i in soup.find_all('li')[:2]],
                             soup.find('span', id='in_stock').text.split(':')[-1].strip(),
                             soup.find('span', id='price').text, soup.find('span', id='old_price').text, url])