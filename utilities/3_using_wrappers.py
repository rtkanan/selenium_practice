from selenium import webdriver
from handy_wrappers import HandyWrappers
import time


class UsingWrappers1():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        hw = HandyWrappers(driver)
        driver.get(baseUrl)

        textField1 = hw.getElement("name")
        textField1.send_keys("Test")
        time.sleep(2)
        textField2 = hw.getElement("//input[@id='name']", locatorType="xpath")
        textField2.clear()

cdriver = UsingWrappers1()
cdriver.test()