from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

with webdriver.Chrome() as browser:
    current_dir = os.path.abspath(os.path.dirname(
        r'C:\Users\vikto\PycharmProjects\parser_study\Selenium\Автоматизация_тестриования_Seleniium\t.txt'))
    file_path = os.path.join(current_dir, 't.txt')
    browser.get("http://suninjuly.github.io/file_input.html")
    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Petrov")
    browser.find_element(By.NAME, "email").send_keys("ivan@mail")
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(10)
