from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/get_attribute.html')
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    element_input = browser.find_element(By.ID, 'answer').send_keys(y)
    element_r_check = browser.find_element(By.ID, 'robotCheckbox').click()
    element_r_radio = browser.find_element(By.ID, 'robotsRule').click()
    button = browser.find_element(By.XPATH, '/html/body/div/form/div/div/button').click()
    time.sleep(10)
