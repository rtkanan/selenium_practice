from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class DropDown():
    def testDopDown(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        element = driver.find_element_by_id("carselect")
        sel = Select(element)

        # This selects the benz value from select box
        print("Select Benz by value")
        sel.select_by_value("benz")
        time.sleep(2)

        print("Select Honda by index")
        sel.select_by_index(2)
        # sel.select_by_index("2") // both string and integer works!
        time.sleep(2)

        print("Select BMW by visible text")
        sel.select_by_visible_text("BMW")
        time.sleep(2)

cdriver = DropDown()
cdriver.testDopDown()