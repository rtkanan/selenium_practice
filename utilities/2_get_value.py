from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class GetValue():
    def testGetValue(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(2)

        element = driver.find_element_by_id("name")
        print(element.get_attribute("class"))

cdriver = GetValue()
cdriver.testGetValue()