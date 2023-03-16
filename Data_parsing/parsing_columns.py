from bs4 import BeautifulSoup
import requests
import lxml

response = requests.get(url='https://parsinger.ru/table/5/index.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

sum_of_numbers = []
columns = list(i.text for i in soup.find_all('th'))
for n in range(1, 16):
    sum_of_numbers.append(round(sum((float(i.text) for i in soup.select(f'td:nth-child({n})'))), 3))
for i in range(15):
    dict_of_columns = zip(columns, sum_of_numbers)
print(dict(dict_of_columns))

