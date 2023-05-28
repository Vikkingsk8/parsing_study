import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/window_size/1/')
    browser.set_window_size(555+14, 555+132)
    res = browser.find_element(By.ID, 'result')
    time.sleep(5)
    print(res.text)