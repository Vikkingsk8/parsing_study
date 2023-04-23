from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/7/7.html')
    total = sum([int(num.text).send_keys() for num in browser.find_elements(By.TAG_NAME, 'option')])
    time.sleep(2)
    find_form = browser.find_element(By.ID, 'input_result').send_keys(total)
    browser.find_element(By.CLASS_NAME, 'btn').click()
    time.sleep(5)
