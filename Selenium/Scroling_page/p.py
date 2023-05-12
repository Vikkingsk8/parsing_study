# s = 0
# a = 0
# for i in range(924000, 1000000, 1000):
#     s += i
# print(s)
# for j in range(524, 1000):
#     a += j
# print(a)
#
# print(73074000+362474+12933276)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_1/')
    time.sleep(1)
    total, box_lst = 0, []
    while True:
        for elem in browser.find_element(By.ID, 'scroll-container').find_elements(By.TAG_NAME, 'span'):
            if elem not in box_lst:
                elem.find_element(By.TAG_NAME, 'input').send_keys(Keys.DOWN)
                elem.click()
                total += int(elem.text)
                time.sleep(0.1)
                box_lst.append(elem)
        if elem.get_attribute('class') == 'last-of-list':
            break
    print(total)
