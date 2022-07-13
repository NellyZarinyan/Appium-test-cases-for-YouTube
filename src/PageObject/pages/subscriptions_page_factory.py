from src.TestBase.utils.driver_setup import driver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

class SubscriptionsPage():
    def __init__(self,driver):
        self.driver = driver
        
