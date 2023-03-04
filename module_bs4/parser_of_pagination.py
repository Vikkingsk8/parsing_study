from bs4 import BeautifulSoup
import requests

# url = 'http://parsinger.ru/html/index1_page_1.html'
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# pagen = soup.find('div', class_='pagen').find_all('a')
#
# pagen = [link['href'] for link in soup.find('div', class_='pagen').findAll('a')]
#
# print(pagen)

url = 'http://parsinger.ru/html/index1_page_3.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
shema = 'http://parsinger.ru/html/'
pagen = [link.text for link in soup.find('div', class_='pagen').find_all('a')][-1]

print(pagen)
