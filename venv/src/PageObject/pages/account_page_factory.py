from src.PageObject.constants.account_consts import selectorss_account_page
from src.TestBase.utils.driver_setup import driver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


class AccountPage():
    def __init__(self, driver):
        self.driver = driver
        self.close = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=selectorss_account_page['CLOSE_BUTTON'])

    def click_on_close(self):
        self.close.click()
