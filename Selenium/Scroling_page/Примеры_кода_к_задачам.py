from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_1/')

    result = []
    scroll_elem = browser.find_element(By.XPATH, " //*[@id='scroll-container']/div")

    while True:
        ActionChains(browser).move_to_element(scroll_elem).scroll_by_amount(1, 500).perform()
        time.sleep(1)
        if any(elem.get_attribute('class') == 'last-of-list' for elem in browser.find_elements(By.TAG_NAME, 'span')):
            break

    print(sum(int(elem.text) for elem in browser.find_elements(By.TAG_NAME, 'span') if elem.text.isdigit()))


import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

total = []
x = 0
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_1/')
    while x < 100:
        elements = [x for x in browser.find_element(By.ID, 'scroll-container').find_elements(By.TAG_NAME, 'input')]
        for tag in elements:
            if tag not in total:
                time.sleep(1)
                tag.send_keys(Keys.DOWN)
                tag.click()
                total.append(tag)
                x += 1


    lst = [int(x.text) for x in browser.find_element(By.ID, 'scroll-container').find_elements(By.TAG_NAME, 'span')]
    print(sum(lst))



# import time
# from selenium.webdriver import Keys
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# url = 'http://parsinger.ru/infiniti_scroll_1/'
# with webdriver.Chrome() as browser:
#     browser.get(url)
#     time.sleep(0.5)
#     count = 0
#     checking = []
#     result = []
#     while True:
#         input_list = [x for x in browser.find_element(By.ID, 'scroll-container').find_elements(By.TAG_NAME, 'input')]
#
#         for inp in input_list:
#             if inp not in checking:
#                 inp.send_keys(Keys.DOWN)
#                 count += 1
#                 checking.append(inp)
#
#
#         break_loop = [x for x in browser.find_elements(By.TAG_NAME, 'span') if x.get_attribute('class')]
#         if break_loop:
#             break
#     span_list = [result.append(int(x.text)) for x in
#                  browser.find_element(By.ID, 'scroll-container').find_elements(By.TAG_NAME, 'span')]
#     print(f'Результат: {sum(result)}')