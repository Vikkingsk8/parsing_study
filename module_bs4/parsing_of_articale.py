from bs4 import BeautifulSoup
import requests
import lxml

result = []
for i in range(1, 5):
    response = requests.get(url=f'https://parsinger.ru/html/index3_page_{i}.html')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    res = [link['href'] for link in soup.find('div', class_='item_card').findAll('a', class_='name_item')]
print(res)
#     for link in res:
#         response = requests.get(url=f'https://parsinger.ru/html/{link}')
#         response.encoding = 'utf-8'
#         soup = BeautifulSoup(response.text, 'lxml')
#         article = soup.find('p', class_='article')
#         result.append(int(article.text.split()[1]))
# print(sum(result))
#
# print(sum(result))
# summa = 0
# for i in result:
#     for j in i:
#         summa += j
# print(summa)
