from selenium import webdriver
import time

with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/methods/3/index.html')
    cookies = webdriver.get_cookies()
    total = 0
    for cookie in cookies:
        if int(cookie['name'].split('_')[-1]) % 2 == 0:
            total += int(cookie['value'])

    print(total)
