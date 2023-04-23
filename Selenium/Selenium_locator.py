# from selenium import webdriver
# import time
# browser = webdriver.Chrome()
# browser.get('http://parsinger.ru/html/watch/1/1_1.html')
# button = browser.find_element_by_id("sale_button").click()
# time.sleep(10)
# ___________________________________________________
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# browser = webdriver.Chrome()
# browser.get('http://parsinger.ru/html/watch/1/1_1.html')
# button = browser.find_element(By.ID, "sale_button").click()
#
# time.sleep(10)
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# browser.get('http://parsinger.ru/html/watch/1/1_1.html')
# button = browser.find_element(By.ID, "sale_button")
# time.sleep(2)
# button.click()
# time.sleep(2)
# browser.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# try:
#     browser = webdriver.Chrome()
#     browser.get('http://parsinger.ru/html/watch/1/1_1.html')
#     button = browser.find_element(By.ID, "sale_button")
#     time.sleep(2)
#     button.click()
#     time.sleep(2)
# finally:
#     browser.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/html/watch/1/1_1.html')
#     button = browser.find_element(By.ID, "sale_button")
#     time.sleep(2)
#     button.click()
#     time.sleep(2)

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://parsinger.ru/selenium/3/3.html'
with webdriver.Chrome() as browser:
    browser.get(url)
    link = browser.find_element(By.CSS_SELECTOR, 'p:nth-child(2)')
    print(link.text)