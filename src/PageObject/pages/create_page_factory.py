from src.PageObject.constants.create_consts import selectorss_create_page
from src.TestBase.utils.driver_setup import driver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


class CreatePage():
    def __init__(self, driver):
        self.driver = driver
        self.create_short = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=selectorss_create_page['CRETE_A_SHORT'])
        self.upload_a_video = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=selectorss_create_page['UPLOAD_A_VIDEO'])
        self.go_live = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=selectorss_create_page['GO_LIVE'])
        self.close =  driver.find_element(by=AppiumBy.ID, value=selectorss_create_page['CLOSE'])
        self.create_icon =  driver.find_element(by=AppiumBy.ID, value=selectorss_create_page['CRAETE_ICON'])

    def click_on_close(self):
        self.close.click()
