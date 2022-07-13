from src.PageObject.errors.errors_for_search_page import  errors_for_search_page
from src.PageObject.pages.search_page_factory import *
from src.PageObject.pages.base_page import *
from src.TestBase.utils.driver_setup import driver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
import pytest
import allure


base_page =BasePage(driver)

@allure.title('Verify "Search field" is it open Searched result page')
@allure.description("""
Verify "Search field" is it open Searched result page after searching some text
""")
def test_verify_search_field_result_in_shorts():
    search_page = base_page.click_on_search()
    search_page.fill_search_field("hi")
    assert search_page, errors_for_search_page['searched_page_does_not_existing']
    base_page.click_on_home()


@allure.title('Verify "Back" button on Search page return "Home" page')
@allure.description("""
Verify "Back" button on Search page is it return "Home" page after click it
""")
def test_verify_back_button_on_search_pages():
    search_page = base_page.click_on_search()
    back = search_page.click_on_back()
    assert back, errors_for_search_page['home_page_does_not_opend']





