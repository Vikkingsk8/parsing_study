from selenium import webdriver
from selenium.webdriver.common.by import By
import time


with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/blank/modal/2/index.html")
    time.sleep(1)
    elements = browser.find_elements(By.TAG_NAME, "input")
    result = browser.find_element(By.ID, "result")
    for element in elements:
        element.click()
        time.sleep(0.5)
        browser.switch_to.alert.accept()
        result = browser.find_element(By.ID, "result")
        if result.text.isdigit():
            print(result.text)
            break
        else:
            continue

