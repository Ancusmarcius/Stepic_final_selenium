# from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
# import pytest


# @pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    page.open()
