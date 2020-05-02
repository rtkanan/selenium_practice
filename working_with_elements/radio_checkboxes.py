from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickEvent():
    def radioCheckbox(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(10)

        bmwRadio = driver.find_element_by_id("bmwradio")
        bmwRadio.click()
        time.sleep(2)
        
        benzRadio = driver.find_element_by_id("benzradio")
        benzRadio.click()
        time.sleep(2)

        bmwCheck = driver.find_element_by_id("bmwcheck")
        bmwCheck.click()
        time.sleep(2)
        
        benzCheck = driver.find_element_by_id("benzcheck")
        benzCheck.click()

        # To check the values of the clicked items
        print("BMW Radio: ", bmwRadio.is_selected())
        print("Benz Radio: ", benzRadio.is_selected())
        print("BMW Check: ", bmwCheck.is_selected())
        print("BMW Check: ", benzCheck.is_selected())

cdriver = ClickEvent()
cdriver.radioCheckbox()