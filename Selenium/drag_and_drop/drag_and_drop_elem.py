from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/draganddrop/1/index.html')
    drag = browser.find_element(By.ID, 'draggable')
    drop = browser.find_element(By.ID, 'field2')
    actions = ActionChains(browser)
    actions.drag_and_drop(drag, drop).perform()
    time.sleep(0.5)
    print(browser.find_element(By.ID, 'result').text)
