from pages.disk_page import DiskPage
from pages.locators import BasePageLocators
from pages.locators import DiskPageLocators
from lib.test_data import TestData
import pytest


@pytest.fixture()
def open_main_page(get_browser):
    page = DiskPage(get_browser, TestData.main_url)
    page.open()
    page.go_to_full_screen()
    yield page


# @pytest.mark.flaky(reruns=3)
class TestSendWebRequests:
    def test_send_request_get(self, open_main_page):

        page = open_main_page
        page.solve_captcha()
        page.wait_element_is_presented(*BasePageLocators.LOGIN_ICON_BUTTON, 25)
        page.login()
        page.open_url(TestData.disk_url)
        assert page.element_is_presented(*DiskPageLocators.CREATE_BUTTON)
        page.create_folder()
        page.copy_file()
