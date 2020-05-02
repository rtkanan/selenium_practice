from selenium import webdriver

class ChromeDriverWindows():
    def testDriver(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()

        # Window Maximize
        driver.maximize_window()
        print("Maximize window")

        # Open URL
        driver.get(base_url)
        print("Open the base URL")

        # Get Title
        print("Title of the web page is: " + driver.title)

        # Get the current URL
        print("Current URL is " + driver.current_url)

        # Browser Refresh
        driver.refresh()
        print("Refresh the page using refresh method")

        # Browser Refresh using get method
        driver.get(driver.current_url)
        print("Refresh the page via get method")

        # Open another URL
        driver.get("https://google.com")
        print("Open another URL")
        print("Current URL is " + driver.current_url)

        # Browser back
        driver.back()
        print("Go back the base URL")
        print("Current URL is " + driver.current_url)

        # Browser forward
        driver.forward()
        print("Go forward to open the new URL")
        print("Current URL is " + driver.current_url)

        # Get page source
        driver.page_source
        print("Collect the page source")

        # Browser close - This is to close a window
        # driver.close()

        # Broswer quit - This is to kill the driver close all the active windows
        print("Quit driver")
        driver.quit()

chrome = ChromeDriverWindows()
chrome.testDriver()