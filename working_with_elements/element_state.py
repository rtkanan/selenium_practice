from selenium import webdriver
from selenium.webdriver.common.by import By

class ElementState():
    def testDriver(self):
        base_url = "http//google.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        # Assuming the ID is available, but the field is disabled.
        # In this scenario we can't perform any actions on the identified element.
        searchElement = driver.find_element(By.ID, "disabled_id")

        # To check whether the element is enabled or disabled
        elmState = searchElement.is_enabled() # This returns True if the field is enabled
        print("Element State: ", elmState)


es = ElementState()
es.testDriver()