from src.PageObject.constants.notifications_consts import selectors_notifications_page
from src.TestBase.utils.driver_setup import driver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


class NotificationsPage():
    def __init__(self, driver):
        self.driver = driver
        self.notifications_icon = driver.find_element(by=AppiumBy.XPATH, value=selectors_notifications_page['NOTIFICATIONS_ICON'])
        self.back = driver.find_element(by=AppiumBy.XPATH, value=selectors_notifications_page['BACK'])
        
        
    def click_on_back(self):
        self.back.click()


