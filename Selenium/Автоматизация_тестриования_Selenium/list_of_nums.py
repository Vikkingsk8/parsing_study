from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def summa(x, y):
    return int(x) + int(y)


with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/selects1.html')
    elem_x = browser.find_element(By.ID, 'num1')
    elem_y = browser.find_element(By.ID, 'num2')
    x, y = elem_x.text,  elem_y.text
    res = summa(x, y)
    browser.find_element(By.ID, 'dropdown').click()
    browser.find_element(By.CSS_SELECTOR, f'[value="{res}"]').click()
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    time.sleep(5)

