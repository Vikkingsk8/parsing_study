from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/infiniti_scroll_3/')

    total = 0
    summa = 0
    res = []
    while total < 500:
        for i in range(1, 6):
            elements = webdriver.find_element(By.XPATH, f" //*[@id='scroll-container_{i}']/div")
            ActionChains(webdriver).move_to_element(elements).scroll_by_amount(1, 500).perform()
            time.sleep(0.1)
            for element in webdriver.find_elements(By.TAG_NAME, 'span'):
                if element.text.isdigit() and int(element.text) not in res:
                    summa += int(element.text)
                    res.append(int(element.text))
                    total += 1
            if any(element.get_attribute('class') == 'last-of-list' for element in
                   webdriver.find_elements(By.TAG_NAME, 'span.')):
                break
    print(summa)
