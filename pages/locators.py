from selenium.webdriver.common.by import By
from lib.test_data import TestData


class BasePageLocators:
    ROBOT_CHECKBOX = (By.CSS_SELECTOR, '.CheckboxCaptcha-Button')
    LOGIN_ICON_BUTTON = (By.CSS_SELECTOR, '.base-button__rootElement-12.base-button__m-2y.'
                                          'base-button__regular--M')
    WITH_YANDEX_ID_BUTTON = (By.CSS_SELECTOR, '.login-content__yaButtonWrapper-15 .base-login-button_'
                                              '_loginButton-xC.login-content__yaButton-2A')
    LOGIN_WITH_EMAIL_BUTTON = (By.CSS_SELECTOR, '.AuthLoginInputToggle-wrapper .AuthLogin'
                                                'InputToggle-type:nth-child(1)')
    LOGIN_FIELD = (By.ID, 'passp-field-login')
    PASSWORD_FIELD = (By.ID, 'passp-field-passwd')
    QUESTION_FIELD = (By.ID, 'passp-field-question')
    LOGIN_BUTTON = (By.CLASS_NAME, 'Button2_type_submit')

    SEARCH_FIELD = (By.CSS_SELECTOR, '.dzen-desktop__search-37 .dzen-search-arrow-common')
    SEARCH_FIELD_FOR_INPUT = (By.XPATH, '/html/body/form/input[1]')
    FIRST_ELEMENT_IN_SEARCH = (By.CSS_SELECTOR, '.arrow__input.mini-suggest__input')
    DISK_BUTTON = (By.CSS_SELECTOR, '#services-big-item-disk-title')


class DiskPageLocators:
    CREATE_BUTTON = (By.CSS_SELECTOR, '.LeftColumn__Buttons .Button2.Button2_view_'
                                      'raised.Button2_size_m.Button2_width_max')
    FOLDER_BUTTON = (By.CSS_SELECTOR, '.file-icon.file-icon_size_m.file-icon_'
                                      'dir_plus.create-resource-button__icon')
    FOLDER_NAME_FIELD = (By.CSS_SELECTOR, '.Textinput_view_default .Textinput-Control')
    SAVE_BUTTON = (By.CLASS_NAME, 'confirmation-dialog__button_submit')
    FILE_FOR_COPY = (By.CSS_SELECTOR, '.listing-item:nth-child(1)')
    COPY_BUTTON = (By.CLASS_NAME, 'groupable-buttons__visible-button_name_copy')
    NEW_FOLDER_IN_COPY_MENU = (By.CSS_SELECTOR, f'[title="{TestData.folder_name}"]')
    MOVE_SUBMIT_BUTTON = (By.CLASS_NAME, 'confirmation-dialog__button_submit')
    NEW_FOLDER_IN_ROOT_LIST = (By.CSS_SELECTOR, f'.listing-item__title[aria-label="{TestData.folder_name}"]')
