from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickEvent():
    def testDriver(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)

        # This is time to wait before the field get's loaded for each element
        driver.implicitly_wait(10)

        # To click the button
        loginLink = driver.find_element(By.XPATH, "//a[@href='/sign_in']")
        loginLink.click()

        # To enter text in the text field
        emailField = driver.find_element(By.ID, "user_email")
        emailField.send_keys("test@test.com")

        passwordField = driver.find_element(By.ID, "user_password")
        passwordField.send_keys("test")

        time.sleep(3)

        # Clear the text from input text field
        emailField.clear()

        time.sleep(3)
        emailField.send_keys("test@test.com")

        submitButton = driver.find_element(By.XPATH, "//input[@type='submit']")
        submitButton.click()

        # driver.quit()

cdriver = ClickEvent()
cdriver.testDriver()