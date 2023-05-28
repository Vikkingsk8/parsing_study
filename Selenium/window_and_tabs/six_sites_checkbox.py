from selenium import webdriver
from selenium.webdriver.common.by import By
from math import sqrt
import time

sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html',
         'http://parsinger.ru/blank/1/3.html',
         'http://parsinger.ru/blank/1/4.html', 'http://parsinger.ru/blank/1/5.html',
         'http://parsinger.ru/blank/1/6.html', ]

res = 0
with webdriver.Chrome() as browser:
    for counter, site in enumerate(sites):
        browser.execute_script(f'window.open("{site}", "_blank_{counter}");')
        time.sleep(0.5)

    for x in range(1, len(browser.window_handles)):
        browser.switch_to.window(browser.window_handles[x])
        browser.find_element(By.CSS_SELECTOR, 'input[class="checkbox_class"]').click()
        res += sqrt(int(browser.find_element(By.ID, 'result').text))
    print(round(res, 9))
    # for handle in browser.window_handles:
    #     browser.switch_to.window(handle)
    #     browser.find_element(By.CSS_SELECTOR, 'input[class="checkbox_class"]').click()
    #     res += sqrt(int(browser.find_element(By.ID, 'result').text))
    #
    # print(res)
