from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/draganddrop/2/index.html')
    drag = driver.find_element(By.ID, 'draggable')
    element = driver.find_elements(By.CLASS_NAME, 'box')
    actions = ActionChains(driver)
    for elem in element:
        actions.drag_and_drop(drag, elem).perform()
        time.sleep(1)
    print(driver.find_element(By.ID, 'message').text)