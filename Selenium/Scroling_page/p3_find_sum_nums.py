from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get("https://parsinger.ru/scroll/3/")
    elements = driver.find_elements(By.TAG_NAME, "input")
    numbers_id = driver.find_elements(By.TAG_NAME, "id")
    res = 0
    for element in elements:
        element.click()

    lst = driver.find_elements(By.TAG_NAME, 'span')
    for index, elem in enumerate(lst):
        if elem.text.isdigit():
            res += index+1
print(res)
# from selenium.webdriver import Keys
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# result = []
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/scroll/3/')
#
#     tag_input = browser.find_elements(By.TAG_NAME, 'input')
#     tag_span = browser.find_elements(By.TAG_NAME, 'span')
#
#     for ti, ts in zip(tag_input, tag_span):
#         ti.send_keys(Keys.DOWN)
#         ti.click()
#         if ts.text:
#             result.append(int(ti.get_attribute('id')))
#
# print(sum(result))
