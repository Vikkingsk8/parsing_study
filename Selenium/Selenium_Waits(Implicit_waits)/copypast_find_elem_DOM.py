from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/expectations/6/index.html')
    element = WebDriverWait(browser, 10).until(ES.element_to_be_clickable((By.ID, 'btn'))).click()
    res = WebDriverWait(browser, 30).until(ES.presence_of_element_located((By.CLASS_NAME, 'Y1DM2GR')))
    if res:
        print(res.text)