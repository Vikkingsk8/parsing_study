from selenium import webdriver
from selenium.webdriver.common.by import By
import time


with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/scroll/2/index.html')
    elements = webdriver.find_elements(By.TAG_NAME, 'input')
    lst = webdriver.find_elements(By.TAG_NAME, 'span')
    res = []
    for element in elements:
        element.click()

    for index, elem in enumerate(lst):
        if elem.text.isdigit():
                res.append(elem.text)
print(res)





