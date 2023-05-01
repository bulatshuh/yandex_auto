from pages.main_page import MainPage
from pages.locators import MainPageLocators
from pages.locators import DiskPageLocators
import pytest
import time


@pytest.fixture()
def open_main_page(get_browser):
    page = MainPage(get_browser, 'https://yandex.ru')
    page.open()
    page.go_to_full_screen()
    yield page


# @pytest.mark.flaky(reruns=3)
class TestSendWebRequests:
    def test_send_request_get(self, open_main_page):

        page = open_main_page
        page.solve_captcha()
        page.wait_element_is_presented(*MainPageLocators.LOGIN_ICON_BUTTON, 25)
        page.login()
        page.open_disk()
        assert page.element_is_presented(*DiskPageLocators.CREATE_BUTTON)
