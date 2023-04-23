import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/4/4.html')
    button = browser.find_element(By.CLASS_NAME, 'btn')
    click = [check.click() for check in browser.find_elements(By.CLASS_NAME, 'check')]
    time.sleep(2)
    button.click()
    time.sleep(5)

