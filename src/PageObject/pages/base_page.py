from src.PageObject.constants.youtube_consts import selectorss_you_tube
from src.PageObject.pages.account_page_factory import AccountPage
from src.PageObject.pages.library_page_factory import LibraryPage
from src.PageObject.pages.subscriptions_page_factory import SubscriptionsPage
from src.PageObject.pages.shorts_page_factory import ShortsPage
from src.PageObject.pages.notifications_page_factory import NotificationsPage
from src.PageObject.pages.create_page_factory import CreatePage
from src.PageObject.pages.search_page_factory import SearchPage
from src.PageObject.pages.main_page import HomePage
from src.TestBase.utils.driver_setup import driver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.search = driver.find_element(by=AppiumBy.XPATH, value=selectorss_you_tube['SEARCH'])
        self.home = driver.find_element(by=AppiumBy.XPATH, value=selectorss_you_tube['HOME'])
        self.subscriptions = driver.find_element(by=AppiumBy.XPATH, value=selectorss_you_tube['SUBSCRIPTIONS'])
        self.library = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=selectorss_you_tube['LIBRARY'])
        self.shorts = driver.find_element(by=AppiumBy.XPATH, value=selectorss_you_tube['SHORTS'])
        self.account = driver.find_element(by=AppiumBy.XPATH, value=selectorss_you_tube['ACCOUNT'])
        self.youTubeIcon = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=selectorss_you_tube['YOUTUBE_ICON'])
        self.create = driver.find_element(by=AppiumBy.XPATH, value=selectorss_you_tube['CREATE'])
        self.notifications = driver.find_element(by=AppiumBy.XPATH, value=selectorss_you_tube['NOTIFICATIONS'])


    def click_on_search(self):
        self.search.click()
        search_page = SearchPage(self.driver)
        return search_page

    def click_on_home(self):
        self.home.click()
        home_page = HomePage(self.driver)
        return home_page

    def click_on_library(self):
        self.library.click()
        library_page = LibraryPage(self.driver)
        return library_page

    def click_on_subscriptions(self):
        self.subscriptions.click()
        subscriptions_page =  SubscriptionsPage(self.driver)
        return  subscriptions_page

    def click_on_shorts(self):
        self.shorts.click()
        shorts_page = ShortsPage(self.driver)
        return shorts_page

    def click_on_account(self):
        self.account.click()
        account_page = AccountPage(self.driver)
        return account_page

    def click_on_notifications(self):
        self.notifications.click()
        notifications_page = NotificationsPage(self.driver)
        return notifications_page

    def click_on_create(self):
        self.create.click()
        create_page = CreatePage(self.driver)
        return create_page

