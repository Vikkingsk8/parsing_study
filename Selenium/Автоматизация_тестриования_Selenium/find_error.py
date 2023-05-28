from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as driver:
    driver.get('http://suninjuly.github.io/cats.html')
    driver.find_element(By.ID, 'button')
    #selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"css selector","selector":"[id="button"]"}
