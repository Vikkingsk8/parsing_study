from selenium import webdriver
from selenium.webdriver.common.by import By
import time


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/blank/modal/3/index.html')

    for elem in browser.find_elements(By.TAG_NAME, 'input'):
        elem.click()
        time.sleep(0.1)
        alert = browser.switch_to.alert
        pin = alert.text
        alert.accept()
        browser.find_element(By.ID, "input").send_keys(pin)
        browser.find_element(By.ID, 'check').click()
        res = browser.find_element(By.ID, 'result')
        if res.text != 'Неверный пин-код':
            print(res.text)
            break
