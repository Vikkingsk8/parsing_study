from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/methods/5/index.html')
    links = [i.get_attribute('href') for i in webdriver.find_elements(By.TAG_NAME, 'a')]
    total = 0
    res = 0
    for link in links:
        webdriver.get(link)
        time.sleep(1)
        for i in webdriver.get_cookies():
            if int(i['expiry']) > total:
                total = int(i['expiry'])
                result = webdriver.find_element(By.ID, 'result').text
                if int(result) > res:
                    res = int(result)
    print(res)


