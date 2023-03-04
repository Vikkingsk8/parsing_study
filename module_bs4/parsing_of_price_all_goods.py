from bs4 import BeautifulSoup
import requests
import lxml

summa = 0
index_labels = {1: "watch", 2: "mobile", 3: "mouse", 4: "hdd", 5: "headphones"}
for i in range(5):
    for j in range(32):
        url = f"https://parsinger.ru/html/{index_labels[i + 1]}/{i + 1}/{i + 1}_{j + 1}.html"
        response = requests.get(url=url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        for price in soup.find('span', attrs={'id': 'price'}):
            for quantity in soup.find('span', attrs={'id': 'in_stock'}):
                summa += int(price.text.replace(' руб', '')) * int(quantity.text.replace('В наличии: ', ''))
print(summa)
#
# print(result)
#     for link in res:
#         response = requests.get(url=f'https://parsinger.ru/html/{link}')
#         response.encoding = 'utf-8'
#         soup = BeautifulSoup(response.text, 'lxml')
#         article = soup.find('p', class_='article')
#         result.append(int(article.text.split()[1]))
# print(sum(result))
