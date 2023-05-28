from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    browser.execute_script("window.scrollBy(0, 100);")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element(By.ID, "book").click()
    browser.execute_script("window.scrollBy(0, 100);")
    x_elem = browser.find_element(By.ID, "input_value")
    res = calc(x_elem.text)
    input_res = browser.find_element(By.ID, "answer").send_keys(res)
    browser.find_element(By.ID, "solve").click()
    print(browser.switch_to.alert.text)

