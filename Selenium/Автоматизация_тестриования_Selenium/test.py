from selenium import webdriver
from selenium.webdriver.common.by import By
import time




with webdriver.Chrome() as browser:
    # browser.get('http://suninjuly.github.io/math.html')
    # people_radio = browser.find_element(By.ID, "peopleRule")
    # people_checked = people_radio.get_attribute("checked")
    # print("value of people radio: ", people_checked)
    # assert people_checked is not None, "People radio is not selected by default"

    #assert people_checked == "true", "People radio is not selected by default"

    # robots_radio = browser.find_element(By.ID, "robotsRule")
    # robots_checked = robots_radio.get_attribute("checked")
    # assert robots_checked is None

    #browser.execute_script("alert('Robots at work');")

    browser = webdriver.Chrome()
    #browser.execute_script("alert('Robots at work');")
    browser.execute_script("document.title='Script executing';alert('Robots at work');")