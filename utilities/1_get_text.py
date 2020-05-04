from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class GetText():
    def testGetText(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(2)

        element = driver.find_element_by_id("opentab")
        print(element.text)

cdriver = GetText()
cdriver.testGetText()