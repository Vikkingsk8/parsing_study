from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.html')
    char = browser.find_element(By.ID, 'text_box')
    res = eval(char.text)
    res_num = [num.text for num in browser.find_elements(By.TAG_NAME, 'option') if res == int(num.text)]
    time.sleep(2)
    browser.find_element(By.ID, 'selectId').send_keys(res_num)
    browser.find_element(By.CLASS_NAME, 'btn').click()
    time.sleep(5)
