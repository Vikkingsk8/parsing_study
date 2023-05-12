from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string

with webdriver.Chrome() as webdriver:
    webdriver.get("http://suninjuly.github.io/huge_form.html")
    elements = webdriver.find_elements(By.TAG_NAME, "input")
    letters = string.ascii_lowercase
    random_words = ''.join(random.choice(letters) for _ in range(8))
    for element in elements:
        element.send_keys(random_words)
    webdriver.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(5)
