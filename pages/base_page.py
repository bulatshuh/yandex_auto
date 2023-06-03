from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators
from lib.test_data import TestData


class BasePage:
    def __init__(self, browser, url, timeout=4):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def go_to_full_screen(self):
        self.browser.maximize_window()

    def element_is_presented(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def element_is_not_presented(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            print('Вышло окно проверки робота!')
            return True
        return False

    def wait_element_is_presented(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def wait_element_is_clickable(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            return False
        return True

    def scroll_down(self, height):
        self.browser.execute_script(f"window.scrollTo(0, {height})")

    def open_url(self, url_new):
        self.browser.get(url_new)

    def switch_to_first_tab(self):
        self.browser.switch_to.window(self.browser.window_handles[0])

    def solve_captcha(self):
        try:
            check_box = self.browser.find_element(*BasePageLocators.ROBOT_CHECKBOX)
        except NoSuchElementException:
            pass
        else:
            check_box.click()

    def login(self):
        login_icon = self.browser.find_element(*BasePageLocators.LOGIN_ICON_BUTTON)
        login_icon.click()
        self.browser.find_element(*BasePageLocators.WITH_YANDEX_ID_BUTTON).click()
        self.browser.find_element(*BasePageLocators.LOGIN_WITH_EMAIL_BUTTON).click()
        login_field = self.browser.find_element(*BasePageLocators.LOGIN_FIELD)
        login_field.send_keys(TestData.login)
        self.browser.find_element(*BasePageLocators.LOGIN_BUTTON).click()
        password_field = self.browser.find_element(*BasePageLocators.PASSWORD_FIELD)
        password_field.send_keys(TestData.password)
        self.browser.find_element(*BasePageLocators.LOGIN_BUTTON).click()
        try:
            question_field = self.browser.find_element(*BasePageLocators.QUESTION_FIELD)
        except NoSuchElementException:
            pass
        else:
            question_field.send_keys(TestData.answer)
            self.browser.find_element(*BasePageLocators.LOGIN_BUTTON).click()
