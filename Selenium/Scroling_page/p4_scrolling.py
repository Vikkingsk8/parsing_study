# Откройте сайт с помощью Selenium;
# На сайте есть список из 100 элементов, которые генерируются при скроллинге;
# В списке есть интерактивные элементы, по которым можно осуществить скроллинг вниз;
# Используйте Keys.DOWN или .move_to_element();
# Цель: получить все значение в элементах, сложить их;
# Получившийся результат вставить в поле ответа.
# Подсказка:
#
# Элементы могут грузится медленнее чем работает ваш код, установите задержки.
#
# Подумайте над условием прерывания цикла, последний элемент в списке имеет class="last-of-list"


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/infiniti_scroll_1/')
    elements = webdriver.find_element(By.ID, "scroll-container").find_elements(By.TAG_NAME, 'input')
    result, res = [], []

    while True:
        for element in elements:
            if element not in result:
                webdriver.execute_script("return arguments[0].scrollIntoView(true);", element)
                element.click()
                time.sleep(0.1)

        for i in webdriver.find_element(By.ID, "scroll-container").find_elements(By.TAG_NAME, 'span'):
            if i not in res:
                res.append(i.text)

print(res)
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import Keys
# import time
#
# with webdriver.Chrome() as browser:
#     browser.get('https://parsinger.ru/infiniti_scroll_1/')
#     time.sleep(1)
#     total, box_lst = 0, []
#     while True:
#         for elem in browser.find_element(By.ID, 'scroll-container').find_elements(By.TAG_NAME, 'span'):
#             if elem not in box_lst:
#                 elem.find_element(By.TAG_NAME, 'input').send_keys(Keys.DOWN)
#                 total += int(elem.text)
#                 time.sleep(0.1)
#                 box_lst.append(elem)
#         if elem.get_attribute('class') == 'last-of-list':
#             break
#     print(total)
