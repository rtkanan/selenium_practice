from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ListOfElements():
    def elementsList(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        radioList = driver.find_elements(
            By.XPATH,
            "//input[contains(@type, 'radio') and contains(@name, 'cars')]")
        print(len(radioList))

        for rbutton in radioList:
            isSelected = rbutton.is_selected()

            if not isSelected:
                rbutton.click()
                time.sleep(3)

cdriver = ListOfElements()
cdriver.elementsList()