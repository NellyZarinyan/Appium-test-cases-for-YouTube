from src.PageObject.constants.search_consts import selectorss_shorts_page
from src.PageObject.pages.searched_result_page_factory import SearchedResultPage
from src.PageObject.pages.main_page import HomePage
from src.TestBase.utils.driver_setup import driver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


class SearchPage():
    def __init__(self, driver):
        self.driver = driver
        self.back = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=selectorss_shorts_page['BACK'])
        self.search_field = driver.find_element(by=AppiumBy.ID, value=selectorss_shorts_page['SEARCH_FIELD'])

    def click_on_back(self):
        self.back.click()
        home_page = HomePage(self.driver)
        return home_page

    def fill_search_field(self, value):
        self.search_field.send_keys(value)
        self.driver.keyevent(66)
        serached_page = SearchedResultPage(self.driver)
        return serached_page
