import requests
import lxml
from bs4 import BeautifulSoup

response = requests.get(url='https://parsinger.ru/table/1/index.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
result = sum(set((float(i.text) for i in soup.find('table').find_all('td'))))
print(result)
