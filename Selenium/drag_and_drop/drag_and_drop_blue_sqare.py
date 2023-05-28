from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait
import time

with webdriver.Chrome() as driver:
    driver.get("https://parsinger.ru/draganddrop/3/index.html")
    element = driver.find_element(By.ID, "block1")
    target_elements = driver.find_elements(By.CLASS_NAME, "controlPoint")
    actions = ActionChains(driver)
    for elem in target_elements:
        actions.click_and_hold(element).move_by_offset(50, -0.5).release().perform()
        time.sleep(0.5)
    res = WebDriverWait(driver, 20).until(ES.visibility_of_element_located((By.ID, "message"))).text
    print(res)
