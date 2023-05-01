from selenium.webdriver.common.by import By


class MainPageLocators:
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
    SEARCH_FIELD_FOR_INPUT = (By.CSS_SELECTOR, '.body_search_yes .mini-suggest .arrow__input')
    FIRST_ELEMENT_IN_SEARCH = (By.CSS_SELECTOR, '.mini-suggest__item_subtype_base')
    DISK_BUTTON = (By.CSS_SELECTOR, '#services-big-item-disk-title')


class DiskPageLocators:
    CREATE_BUTTON = (By.CSS_SELECTOR, '.Button2.Button2_view_raised.Button2_size_m.Button2_width_max')
    FOLDER_BUTTON = (By.CSS_SELECTOR, '.file-icon.file-icon_size_m.file-icon_'
                                      'dir_plus.create-resource-button__icon')
    FOLDER_NAME_FIELD = (By.CSS_SELECTOR, '.Textinput.Textinput_view_default.Textinput_size_m')
    SAVE_BUTTON = (By.CLASS_NAME, 'confirmation-dialog__button_submit')
    FILE_FOR_COPY = (By.CSS_SELECTOR, '[aria-label="Файл для копирования.txt"]')
    MOVE_BUTTON = (By.CLASS_NAME, 'groupable-buttons__visible-button_name_move')
    NEW_FOLDER = (By.CSS_SELECTOR, '[title="Новая папка"]')
    MOVE_SUBMIT_BUTTON = (By.CLASS_NAME, 'confirmation-dialog__button_submit')
    # RENAME_BUTTON = (By.CLASS_NAME, 'groupable-buttons__visible-button_name_rename')
    ANY_ELEMENT = (By.CSS_SELECTOR, '.listing-item__info')
    ANY_ELEMENT_PLUS = (By.CSS_SELECTOR, '.listing-item__title.listing-item__title_overflow_clamp')
