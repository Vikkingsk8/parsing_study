import requests
import lxml
from bs4 import BeautifulSoup

response = requests.get(url='https://parsinger.ru/table/2/index.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
result = sum((float(i.text) for i in soup.select('td:first-child')))
print(result)
