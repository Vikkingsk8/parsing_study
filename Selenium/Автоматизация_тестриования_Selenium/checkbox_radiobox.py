from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get('https://suninjuly.github.io/math.html')
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    element_input = browser.find_element(By.ID, 'answer').send_keys(y)
    element_r_check = browser.find_element(By.ID, 'robotCheckbox').click()
    element_r_radio = browser.find_element(By.ID, 'robotsRule').click()
    button = browser.find_element(By.XPATH, '/html/body/div/form/button').click()
    time.sleep(10)
