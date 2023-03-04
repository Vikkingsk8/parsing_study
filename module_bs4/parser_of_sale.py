from bs4 import BeautifulSoup
import requests
import lxml

response = requests.get(url='https://parsinger.ru/html/hdd/4/4_1.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

new_price = soup.find('span', attrs={'id': 'price'})
old_price = soup.find('span', attrs={'id': 'old_price'})
new_price = int(new_price.text.replace(' руб', ''))
old_price = int(old_price.text.replace(' руб', ''))
sale = round((old_price - new_price) * 100 / old_price, 1)
print(sale)
