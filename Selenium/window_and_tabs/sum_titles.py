from selenium import webdriver
from selenium.webdriver.common.by import By


res = 0
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/blank/3/index.html')

    [b.click() for b in browser.find_elements(By.TAG_NAME, 'input')]

    for handle in browser.window_handles:
        browser.switch_to.window(handle)
        title = browser.execute_script("return document.title;")
        res += int(title) if title.isdigit() else 0
    print(res)



