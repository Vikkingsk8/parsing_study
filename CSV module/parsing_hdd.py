import csv
import requests
from bs4 import BeautifulSoup
import time

start = time.time() ## точка отсчета времени
# first part create file csv with headers
with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([
        'Наименование', 'Бренд',
        'Форм-фактор', 'Ёмкость', 'Объем буферной памяти', 'Цена' ])

# part 2

for i in range(1, 5):
    url = f'https://parsinger.ru/html/index4_page_{i}.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    name = [n.text.strip() for n in soup.find_all('a', attrs={'class': 'name_item'})]
    description = [d.text.split('\n') for d in soup.find_all('div', class_='description')]
    price = [p.text for p in soup.find_all('p', class_='price')]

# part 3

    for item, price, descr in zip(name, price, description):
        flatten = item,  *[x.split(':')[1].strip().replace('.', ',') for x in descr if x], price

        open('res.csv', 'a', encoding='utf-8-sig', newline='')
        writer = csv.writer(file, delimiter=';')
        writer.writerow(flatten)
file.close()
print('Файл res.csv создан')

##код программы

end = time.time() - start ## собственно время работы программы

print(end) ## вывод времени