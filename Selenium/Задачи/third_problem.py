from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.html')
    find_tag = browser.find_elements(By.TAG_NAME, 'p')
    total = 0
    for num in find_tag:
        total += int(num.text)
    print(total)
