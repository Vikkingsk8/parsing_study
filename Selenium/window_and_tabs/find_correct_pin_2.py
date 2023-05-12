from selenium import webdriver
from selenium.webdriver.common.by import By
import time


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/blank/modal/4/index.html')

    for pin in browser.find_elements(By.TAG_NAME, 'span'):
        p = pin.text
        browser.find_element(By.ID, 'check').click()
        time.sleep(0.1)
        promt = browser.switch_to.alert
        promt.send_keys(p)
        promt.accept()
        res = browser.find_element(By.ID, 'result')
        if res.text != 'Неверный пин-код':
            print(res.text)
            break