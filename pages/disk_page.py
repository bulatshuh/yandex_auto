from .base_page import BasePage
from .locators import DiskPageLocators
import time


class DiskPage(BasePage):
    def create_folder(self):
        self.browser.find_element(*DiskPageLocators.CREATE_BUTTON).click()
        self.browser.find_element(*DiskPageLocators.FOLDER_BUTTON).click()
        folder_name_field = self.browser.find_element(*DiskPageLocators.FOLDER_NAME_FIELD)
        time.sleep(1)
        folder_name_field.send_keys('Name')
        self.browser.find_element(*DiskPageLocators.SAVE_BUTTON).click()

    def copy_file(self):
        file = self.browser.find_element(*DiskPageLocators.FILE_FOR_COPY)
        self.wait_element_is_clickable(*DiskPageLocators.FILE_FOR_COPY)
        file.click()
        self.browser.find_element(*DiskPageLocators.COPY_BUTTON).click()
        self.browser.find_element(*DiskPageLocators.NEW_FOLDER_IN_COPY_MENU).click()
        self.browser.find_element(*DiskPageLocators.MOVE_SUBMIT_BUTTON).click()
        self.browser.find_element(*DiskPageLocators.NEW_FOLDER_IN_ROOT_LIST).click()
        time.sleep(5)
