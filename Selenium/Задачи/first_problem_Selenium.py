from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/1/1.html')
    input_form = browser.find_elements(By.CLASS_NAME, 'form')
    for elem in input_form:
        elem.send_keys('Text')
    button = browser.find_element(By.ID, 'btn')
    time.sleep(1)
    button.click()
    time.sleep(3)

# from selenium.webdriver.common.by import By
# from selenium import webdriver
# from faker import Faker
# import time
#
# хорошее решение
# def fill_input():
#     """Fill the input lines"""
#     with webdriver.Chrome() as browser:
#         url = 'https://parsinger.ru/selenium/1/1.html'
#         browser.get(url)
#         fake = Faker()
#         form_list = [fake.name(), fake.last_name(), fake.name(),
#                      fake.random_int(min=18, max=99, step=1), fake.city(), fake.email()]
#         forms = browser.find_elements(By.CLASS_NAME, 'form')
#         button = browser.find_element(By.ID, 'btn')
#         for input_data, form in zip(form_list, forms):
#             form.send_keys(input_data)
#         button.click()
#         time.sleep(5)
#
#
# if __name__ == "__main__":
#     fill_input()
