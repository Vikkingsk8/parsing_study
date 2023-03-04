from bs4 import BeautifulSoup
import requests
import lxml

response = requests.get(url='https://parsinger.ru/html/watch/1/1_4.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

p_attr = soup.find('span', attrs={'id': 'price'})
print(p_attr.text.replace(' руб', ''))
# print(p_attr)
# print(soup)
# count = 0
# for i in p_attr:
#     i = i.text.replace(' руб','')
#     count += int(i)
# print(count)