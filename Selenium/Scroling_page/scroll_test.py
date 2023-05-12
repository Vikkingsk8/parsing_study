# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/scroll/1/')
#     browser.execute_script('window.scrollBy(0, 5000)')
#     for i in range(10):
#         browser.execute_script('window.scrollBy(0, 5000)')
#         time.sleep(3)


# import time
# from selenium import webdriver
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/scroll/1/')
#     height = browser.execute_script("return document.body.scrollHeight")
#     time.sleep(2)
#     print(height)
#
# from selenium import webdriver
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/scroll/1/')
#     height = browser.execute_script("return window.innerHeight")
#     print(height)
import time
from selenium import webdriver

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/1/')
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)