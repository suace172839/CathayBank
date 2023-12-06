from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


implicitlyWaitTime = 10
restartBrowserTime = 5

class Web():
    def __init__(self, url):
        # Open wbepage via Chrome.
        self.driver = webdriver.Chrome()
        # Wait no more than 20 seconds for webpage loading
        self.driver.implicitly_wait(implicitlyWaitTime)
        self.driver.get(url)
    
    def __del__(self):
        self.driver.close()

    def close(self):
        self.driver.close()
        # Wait 5 seconds before restart browser.
        sleep(restartBrowserTime)

    def find_element(self, locator, pattern):
        return self.driver.find_element(locator, pattern)
    
    def find_elements(self, locator, pattern):
        return self.driver.find_elements(locator, pattern)

    def click(self, element):
        ActionChains(self.driver).move_to_element(element).click().perform()

    def screenshot(self, path):
        self.driver.get_screenshot_as_file(path)

