from bs4 import BeautifulSoup
import requests
import lxml

response = requests.get(url='https://parsinger.ru/html/index1_page_1.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

p_attr = soup.findAll('p', attrs={'class': 'price'})
# print(p_attr)
# print(soup)
count = 0
for i in p_attr:
    i = i.text.replace(' руб','')
    count += int(i)
print(count)

