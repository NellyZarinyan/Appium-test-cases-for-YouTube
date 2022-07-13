from src.PageObject.constants.shorts_consts import selectorss_shorts_page
from src.TestBase.utils.driver_setup import driver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

class ShortsPage():
    def __init__(self, driver):
        self.driver = driver
        self.like = driver.find_element(by=AppiumBy.ID, value=selectorss_shorts_page['LIKE'])
        self.dislike = driver.find_element(by=AppiumBy.ID, value=selectorss_shorts_page['DISLIKE'])
        self.comments = driver.find_element(by=AppiumBy.ID, value=selectorss_shorts_page['COMMENTS'])
        self.share = driver.find_element(by=AppiumBy.ID, value=selectorss_shorts_page['SHARE'])
        self.back = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=selectorss_shorts_page['BACK'])
        self.video = driver.find_element(by=AppiumBy.ID, value=selectorss_shorts_page['SHORTS_VIDEO'])

    
    def click_on_back(self):
        self.back.click()

    def stop_video(self):
        self.video.click()