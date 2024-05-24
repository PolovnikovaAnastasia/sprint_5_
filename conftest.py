from selenium import webdriver

import pytest
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()