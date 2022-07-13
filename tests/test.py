from src.PageObject.errors.errors_for_test import error_tests
from src.PageObject.pages.subscriptions_page_factory import *
from src.PageObject.pages.shorts_page_factory import *
from src.PageObject.pages.account_page_factory import *
from src.PageObject.pages.base_page import *
from src.PageObject.pages.notifications_page_factory import *
from src.TestBase.utils.driver_setup import driver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
import  pytest
import  allure


base_page = BasePage(driver)

@allure.title('Verify "Search" button')
@allure.description("""
Check if "Search" button is existing
""")
def test_serch_button_is_displayed():
    driver.implicitly_wait(360)
    assert  base_page.search.is_displayed(), error_tests['sarch_button_ does_not_exist']


@allure.title('Verify "Account" button')
@allure.description("""
Check if "Account" icon is existing
""")
def test_account_icon_is_displayed():
    assert  base_page.account.is_displayed(), error_tests['account_icon_does_not_exist']


@allure.title('Verify "YouTube" icon')
@allure.description("""
Check if "YouTube" icon exist
""")
def test_youtube_icon_is_displayed():
    assert  base_page.youTubeIcon.is_displayed(),error_tests['youTube_icon_does_not_exist']



@allure.title('Verify "Create" button')
@allure.description("""
Check if "Create" button is existing
""")
def test_create_button_is_displayed():
    assert  base_page.create.is_displayed(), error_tests['create_button_does_not_exist']


@allure.title('Verify "Notifications" button ')
@allure.description("""
Check if "Notifications" button is existing
""")
def test_notifications_button_is_displayed():
    assert  base_page.notifications.is_displayed(), error_tests['notifications_button_does_not_exist']


@allure.title('Verify "Subscriptions" button ')
@allure.description("""
Check if "Subscriptions" button is existing 
""")
def test_shubscriptions_button_is_displayed():
    assert  base_page.subscriptions.is_displayed(), error_tests['subscriptions_button_does_not_exist']

@allure.title('Verify "Shorts" button')
@allure.description("""
Check if "Shorts" button 
""")
def test_shorts_button_is_displayed():
    assert  base_page.shorts.is_displayed(), error_tests['shorts_button_does_not_exist']



@allure.title('Verify "Home" button ')
@allure.description("""
Check if "Home" button is existing 
""")
def test_home_button_is_displayed():
    assert  base_page.home.is_displayed(), error_tests['home_button_does_not_exist']



@allure.title('Verify "Library" button')
@allure.description("""
Check if "Library" button is existing 
""")
def test_library_button_is_displayed():
    assert  base_page.library.is_displayed(), error_tests['library_button_does_not_exist']


@allure.title('Verify "Shorts" page')
@allure.description("""
Check if "Shorts" page opend videos
""")
def test_verify_shorts_paeg():
    shorts_page = base_page.click_on_shorts()
    assert shorts_page, error_tests['shorts_page_does_not_existing']
    shorts_page.click_on_back()


@allure.title('Verify "Subscriptions" page')
@allure.description("""
Check if "Subscriptions" page existing
""")
def test_verify_subscriptions_page():
    subscriptions_page = base_page.click_on_subscriptions()
    assert subscriptions_page, error_tests['subscriptions_page_does_not_existing']


@allure.title('Verify "Library" page')
@allure.description("""
Check if 'Library' page existing
""")
def test_verify_library_page():
    library_page = base_page.click_on_library()
    assert library_page, error_tests['library_page_does_not_existing']


@allure.title('Verify "Account" page')
@allure.description("""
Check if 'Account' page existing
""")
def test_verify_account_page():
    account_page = base_page.click_on_account()
    assert account_page, error_tests['account_page_does_not_existing']
    account_page.click_on_close()


@allure.title('Verify "Notifications" page')
@allure.description("""
Check if "Notifications" page existing
""")
def test_verify_notifications_page():
    notifications_page = base_page.click_on_notifications()
    assert notifications_page, error_tests['notificatins_page_does_not_existing']


@allure.title('Verify "Create" page')
@allure.description("""
Check if "Create" page existing
""")
def test_verify_create_page():
    cerate_page = base_page.click_on_create()
    assert cerate_page, error_tests['create_page_does_not_existing']
    cerate_page.click_on_close()


