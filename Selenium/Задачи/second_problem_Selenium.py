from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/2/2.html')
    find_num = browser.find_element(By.LINK_TEXT, '16243162441624')
    find_num.click()
    time.sleep(5)
