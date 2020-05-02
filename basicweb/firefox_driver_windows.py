from selenium import webdriver

class RunFFTests():
    def testMethod(self):
        # driver = webdriver.Firefox(executable_path="C:\\webdriver\\geckodriver.exe")
        driver = webdriver.Firefox()
        driver.get("https://google.com")

ff = RunFFTests()
ff.testMethod()