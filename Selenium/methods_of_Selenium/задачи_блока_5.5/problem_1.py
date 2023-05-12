from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/1/index.html')
    while True:
        res = browser.find_element(By.ID, 'result')
        if res.text.isdigit():
            print(res.text)
            break
        browser.refresh()
        time.sleep(2)

