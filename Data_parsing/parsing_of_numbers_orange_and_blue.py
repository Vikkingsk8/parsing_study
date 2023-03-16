import requests
import lxml
from bs4 import BeautifulSoup


response = requests.get(url='https://parsinger.ru/table/5/index.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
nums1 = [float(i.text) for i in soup.find_all(class_='orange')]
nums2 = [int(j.text) for j in soup.select('td:last-child')]
summa = sum([a * b for a, b in zip(nums1, nums2)])
print(summa)