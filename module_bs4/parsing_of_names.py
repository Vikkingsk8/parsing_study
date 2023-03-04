from bs4 import BeautifulSoup
import requests
import lxml

goods = []
links = [f'https://parsinger.ru/html/index3_page_{i}.html' for i in range(1, 5)]
#print(links)
for link in links:
    response = requests.get(url=link)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    goods.append([i.text for i in soup.findAll('a', class_='name_item')])

print(goods)

# url = 'https://parsinger.ru/html/'
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# shema = 'http://parsinger.ru/html/'
# pagen = [link.text for link in soup.find('div', class_='pagen').find_all('a')][-1]
#
# print(pagen)
