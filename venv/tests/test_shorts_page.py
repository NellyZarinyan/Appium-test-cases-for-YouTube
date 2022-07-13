from src.PageObject.errors.errors_for_shorts_page import  errors_for_shorts_page
from src.PageObject.pages.shorts_page_factory import *
from src.PageObject.pages.base_page import *
from src.TestBase.utils.driver_setup import driver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
import pytest
import allure


base_page =BasePage(driver)

@allure.title('Verify video on Shorts')
@allure.description("""
verify if on 'Shorts' page existing video
""")
def test_verify_video_in_shorts():
    driver.implicitly_wait(120)
    shorts_page = base_page.click_on_shorts()
    driver.implicitly_wait(120)
    shorts_page.stop_video()
    assert shorts_page.video.is_enabled(), errors_for_shorts_page["video_does_not_enabled"]
    shorts_page.click_on_back()


@allure.title('Verify "Like" button ')
@allure.description("""
verify if on 'Shorts' page existing 'like' button
""")
def test_verify_like_in_shorts():
    driver.implicitly_wait(160)
    shorts_page = base_page.click_on_shorts()
    shorts_page.stop_video()
    assert shorts_page.like.is_enabled(), errors_for_shorts_page["like_button_does_not_enabled"]
    shorts_page.click_on_back()

@allure.title('Verify "Dislike" button ')
@allure.description("""
verify if on 'Shorts' page existing 'dislike' button
""")
def test_verify_dislike_in_shorts():
    driver.implicitly_wait(260)
    shorts_page = base_page.click_on_shorts()
    shorts_page.stop_video()
    assert shorts_page.dislike.is_enabled(), errors_for_shorts_page["dislike_button_does_not_enabled"]
    shorts_page.click_on_back()


@allure.title('Verify "Share" button ')
@allure.description("""
verify if on 'Shorts' page existing 'share' button
""")
def test_verify_share_in_shorts():
    driver.implicitly_wait(260)
    shorts_page = base_page.click_on_shorts()
    shorts_page.stop_video()
    assert shorts_page.share.is_enabled(), errors_for_shorts_page["share_button_does_not_enabled"]
    shorts_page.click_on_back()






