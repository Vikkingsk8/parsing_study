import requests
import lxml
from bs4 import BeautifulSoup


response = requests.get(url='https://parsinger.ru/table/4/index.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
result = sum((float(i.text) for i in soup.find_all(class_='green')))
print(result)