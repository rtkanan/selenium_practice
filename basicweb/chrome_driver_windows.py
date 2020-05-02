from selenium import webdriver

class ChromeDriverWindows():
    def testDriver(self):
        # driver = webdriver.Chrome(executable_path="C:\\webdriver\\chromedriver")
        driver = webdriver.Chrome()
        driver.get("https://google.com")

driver = ChromeDriverWindows()
driver.testDriver()