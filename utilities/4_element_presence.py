from selenium import webdriver
from selenium.webdriver.common.by import By
from handy_wrappers import HandyWrappers
import time


class ElementPresentCheck():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        hw = HandyWrappers(driver)
        driver.get(baseUrl)

        elementResult1 = hw.isElementPresent("name", By.ID)
        print(str(elementResult1))

        elementResult2 = hw.elementPresenceCheck("//input[@id='name1']", By.XPATH)
        print(str(elementResult2))


ff = ElementPresentCheck()
ff.test()