from .base_page import BasePage
from .locators import MainPageLocators
from lib.test_data import login, password, answer
from selenium.common.exceptions import NoSuchElementException
import time


class MainPage(BasePage):
    def solve_captcha(self):
        try:
            check_box = self.browser.find_element(*MainPageLocators.ROBOT_CHECKBOX)
        except NoSuchElementException:
            pass
        else:
            check_box.click()

    def login(self):
        login_icon = self.browser.find_element(*MainPageLocators.LOGIN_ICON_BUTTON)
        login_icon.click()
        self.browser.find_element(*MainPageLocators.WITH_YANDEX_ID_BUTTON).click()
        self.browser.find_element(*MainPageLocators.LOGIN_WITH_EMAIL_BUTTON).click()
        login_field = self.browser.find_element(*MainPageLocators.LOGIN_FIELD)
        login_field.send_keys(login)
        self.browser.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        password_field = self.browser.find_element(*MainPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)
        self.browser.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        try:
            question_field = self.browser.find_element(*MainPageLocators.QUESTION_FIELD)
        except NoSuchElementException:
            pass
        else:
            question_field.send_keys(answer)
            self.browser.find_element(*MainPageLocators.LOGIN_BUTTON).click()

    def open_disk(self):
        field = self.browser.find_element(*MainPageLocators.SEARCH_FIELD)
        field.click()
        search_field = self.browser.find_element(*MainPageLocators.SEARCH_FIELD_FOR_INPUT)
        search_field.send_keys('disk.yandex.ru')
        time.sleep(2)
        self.browser.find_element(*MainPageLocators.FIRST_ELEMENT_IN_SEARCH).click()
