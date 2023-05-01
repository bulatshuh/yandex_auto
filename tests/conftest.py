import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def get_browser():
    browser = webdriver.Chrome()
    print('\nOpening Chrome...')
    yield browser
    print('\nClosing browser...')
    browser.quit()
