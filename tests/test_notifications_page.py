from src.PageObject.errors.errors_for_notifications_page import  errors_for_notifications_page
from src.PageObject.pages.notifications_page_factory import *
from src.PageObject.pages.base_page import *
from src.TestBase.utils.driver_setup import driver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
import pytest
import allure


base_page =BasePage(driver)

@allure.title('Verify icon on "Notifications" page')
@allure.description("""
Verify if on 'Notifications' page existing icon and check it name
""")
def test_verify_icon_in_notificatns():
    notificatons_page = base_page.click_on_notifications()
    assert notificatons_page.notifications_icon.is_displayed(), ['notifications_icon_does_not_exist']
    element = notificatons_page.notifications_icon
    text = element.text
    assert text == 'Notifications', errors_for_notifications_page['icons_text_is_not_"Notifications"']



