from src.PageObject.errors.errors_for_searched_result_page import  errors_for_searched_result_page
from src.PageObject.pages.search_page_factory import *
from src.PageObject.pages.searched_result_page_factory import *
from src.PageObject.pages.base_page import *
from src.TestBase.utils.driver_setup import driver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
import pytest
import allure


base_page =BasePage(driver)

@allure.title('Verify Searched result')
@allure.description("""
Verify Searched text if it have some name in Searched page
""")
def test_verify_search_field_result_in_shorts():
    driver.implicitly_wait(360)
    search_page = base_page.click_on_search()
    searched_page = search_page.fill_search_field('hi')
    element = searched_page.searched_field
    text = element.text
    assert text == 'hi', errors_for_searched_result_page['field_text_is_not_matched']
    base_page.click_on_home()



@allure.title('Verify "Back" button on Searched result page return "Home" page')
@allure.description("""
Verify "Back" button on Searched resylt page is it return "Home" page after click it
""")
def test_verify_back_button_on_searched_result_pages():
    search_page = base_page.click_on_search()
    searched_page = search_page.fill_search_field('hi')
    home_page =  searched_page.click_on_back()
    assert home_page, errors_for_searched_result_page['home_page_does_not_opend']

