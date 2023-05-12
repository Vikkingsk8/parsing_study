from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/infiniti_scroll_2/')
    elements = webdriver.find_element(By.XPATH, " //*[@id='scroll-container']/div")
    res = []

    while True:
        ActionChains(webdriver).move_to_element(elements).scroll_by_amount(1, 500).perform()
        time.sleep(0.5)
        if any(element.get_attribute('class') == 'last-of-list' for element in
               webdriver.find_element(By.ID, 'scroll-container').find_elements(By.TAG_NAME, 'p')):
            break
    print(sum(int(element.text) for element in webdriver.find_elements(By.TAG_NAME, 'p') if element.text.isdigit()))