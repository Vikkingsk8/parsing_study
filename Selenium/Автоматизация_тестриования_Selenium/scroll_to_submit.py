from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/execute_script.html')
    x = browser.find_element(By.ID, 'input_value').text
    res = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(res)
    browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    time.sleep(5)
