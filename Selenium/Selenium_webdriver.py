# from selenium import webdriver
#
# url = 'https://stepik.org/a/104774'
# browser = webdriver.Chrome()
# browser.get(url)

import time
from selenium import webdriver

# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_extension('coords.crx') #'C:\\Users\\vikto\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions\\gkkmpbaijflcgbbdfjgihbgmpkhgpgof\\coords.crx')
# with webdriver.Chrome(options=options_chrome) as browser:
#     url = 'https://yandex.ru/'
#     browser.get(url)
#     time.sleep(50)
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_argument('--headless')
#
# with webdriver.Chrome(options=options_chrome) as browser:
#     url = 'https://yandex.ru/'
#     browser.get(url)
#     a = browser.find_element(By.TAG_NAME, 'a')
#     print(a.get_attribute('href'))
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_extension('coords.crx')
#
#
# options_chrome.add_argument('--headless=chrome')
#
# with webdriver.Chrome(options=options_chrome) as browser:
#     url = 'https://yandex.ru/'
#     browser.get(url)
#     time.sleep(5)
#     a = browser.find_element(By.TAG_NAME, 'a')
#     print(a.get_attribute('href'))
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# proxy = '8.210.83.33:80'
# url = 'https://2ip.ru/'
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=%s' % proxy)
#
# with webdriver.Chrome(options=chrome_options) as browser:
#     browser.get(url)
#     print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
#     time.sleep(5)
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# proxy_list = ['8.210.83.33:80', '199.60.103.28:80',
# '103.151.246.38:10001', '199.60.103.228:80',
# '199.60.103.228:80', '199.60.103.28:80', ]
#
# for PROXY in proxy_list:
#     try:
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument('--proxy-server=%s' % PROXY)
#         url = 'https://2ip.ru/'
#
#         with webdriver.Chrome(options=chrome_options) as browser:
#             browser.get(url)
#             print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
#
#             browser.set_page_load_timeout(5)
#
#             proxy_list.remove(PROXY)
#     except Exception as _ex:
#         print(f"Превышен timeout ожидания для - {PROXY}")
#         continue
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://2ip.ru/'
with webdriver.Chrome() as browser:
    browser.get(url)
    time.sleep(20)
    print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)