from src.PageObject.errors.errors_for_create_page import  errors_for_create_page
from src.PageObject.pages.create_page_factory import *
from src.PageObject.pages.base_page import *
from src.TestBase.utils.driver_setup import driver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
import pytest
import allure



base_page =BasePage(driver)

@allure.title('Verify "Create" button is it open right page')
@allure.description("""
Verify "Create" button is it open "Create" page
""")
def test_verify_create_page():
    driver.implicitly_wait(360)
    create_page = base_page.click_on_create()
    assert create_page, errors_for_create_page['creat_page_is_not_existing']
    create_page.click_on_close()


@allure.title('Verify "Create" buttons icon')
@allure.description("""
Verify "Create" buttons icon is it displayed and have right text
""")
def test_verify_create_icon():
    driver.implicitly_wait(360)
    create_page = base_page.click_on_create()
    assert create_page.create_icon, errors_for_create_page['create_icon_is_not_displayed']
    element = create_page.create_icon
    text = element.text
    assert text == 'Create', errors_for_create_page['icons_text_is_not_matched']
    create_page.click_on_close()


@allure.title('Verify "Create" buttons attributs')
@allure.description("""
Verify "Create" buttons attributs is displed "Create a Short" , "Upload a Vide"  and "Go live" buttons
""")
def test_verify_create_buttons_attributs():
    driver.implicitly_wait(360)
    create_page = base_page.click_on_create()
    assert create_page.create_short.is_displayed(), errors_for_create_page['create_short_button_is_not_displayed']
    assert create_page.upload_a_video.is_displayed(), errors_for_create_page['upload_a_video_button_is_not_displayed']
    assert create_page.go_live.is_displayed(), errors_for_create_page['go_live_button_is_not_displayed']
    create_page.click_on_close()
