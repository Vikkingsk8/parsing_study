from bs4 import BeautifulSoup
import requests
import csv
import time
# запускаем измеритель времени выполнения кода
start = time.time()
# контекстный менеджер для создания csv
with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
# цикл для получения ссылок
    for pagen in range(1,5):
        for category in range(1,6):
            url = f"https://parsinger.ru/html/index{category}_page_{pagen}.html"
            response = requests.get(url=url)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'lxml')
            name = [n.text.strip() for n in soup.find_all('a', attrs={'class': 'name_item'})]
            description = [d.text.split('\n') for d in soup.find_all('div', class_='description')]
            price = [p.text for p in soup.find_all('p', class_='price')]
# формируем информацию в файле csv из полученных ссылок
            for item, price, descr in zip(name, price, description):
                flatten = item, *[x.split(':')[1].strip().replace('.',',') for x in descr if x], price
# записываем всё в файл csv и контекстный менеджер сам закроет документ чтобы информация не потерялась
                writer.writerow(flatten)

print('Файл res.csv создан')
# конец измерения времени выполнения кода
end = time.time() - start
print(end)
