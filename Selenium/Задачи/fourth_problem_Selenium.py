import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.html')
    total = [int(num.text) for num in browser.find_elements(By.CSS_SELECTOR, 'p:nth-child(2)')]
    print(sum(total))
