from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/scroll/4/index.html')
    elements = webdriver.find_elements(By.CLASS_NAME, 'btn')
    res = 0
    for element in elements:
        webdriver.execute_script("return arguments[0].scrollIntoView(true);", element)
        element.click()
        res += int((webdriver.find_element(By.ID, 'result')).text)

print(res)
