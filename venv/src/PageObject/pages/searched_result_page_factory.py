from src.PageObject.constants.searched_result_consts import selectorss_searched_result_page
from src.PageObject.pages.main_page import HomePage
from src.TestBase.utils.driver_setup import driver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


class SearchedResultPage():
    def __init__(self, driver):
        self.driver = driver
        self.searched_field = driver.find_element(by=AppiumBy.ID, value=selectorss_searched_result_page['SEARCH_FIELD'])
        self.back = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=selectorss_searched_result_page['BACK'])

    def click_on_back(self):
        self.back.click()
        home_page = HomePage(self.driver)
        return home_page

