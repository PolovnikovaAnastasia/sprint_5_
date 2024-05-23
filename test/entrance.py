from selenium import webdriver
from locators_web import *
import pytest

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()

# ошибка с неккоректным паролем
def test_registration_form_no_correctly_true(driver):
    driver.find_element(*MainPage.cabinet).click()
    driver.find_element(*MainPage.registration).click()
    driver.find_element(*MainPage.name).send_keys("Анастасия")
    driver.find_element(*MainPage.email).send_keys("polovnikova123@yandex.ru")
    driver.find_element(*MainPage.password).send_keys("12345")
    driver.find_element(*MainPage.entrance).click()
    assert True

# успешная регистрация
def test_registration_form_true(driver):
    driver.find_element(*MainPage.cabinet).click()
    driver.find_element(*MainPage.registration).click()
    driver.find_element(*MainPage.name).send_keys("Анастасия")
    driver.find_element(*MainPage.email).send_keys("polovnikova123@yandex.ru")
    driver.find_element(*MainPage.password).send_keys("123456")
    driver.find_element(*MainPage.entrance).click()
    assert True

# вход по кнопке «Войти в аккаунт» на главной
def test_entrances_true(driver):
    driver.find_element(*MainPage.entrances).click()
    driver.find_element(*MainPage.email1).send_keys("polov12345@yandex.ru")
    driver.find_element(*MainPage.password1).send_keys("123456")
    driver.find_element(*MainPage.authorization).click()
    assert True

# вход через кнопку «Личный кабинет»
def test_lk_true(driver):
    driver.find_element(*MainPage.cabinet).click()
    driver.find_element(*MainPage.email1).send_keys("polov12345@yandex.ru")
    driver.find_element(*MainPage.password1).send_keys("123456")
    driver.find_element(*MainPage.authorization).click()
    assert True

# вход через кнопку в форме регистрации
def test_etrances_reg_true(driver):
    driver.find_element(*MainPage.cabinet).click()
    driver.find_element(*MainPage.registration).click()
    driver.find_element(*MainPage.entrances).click()
    driver.find_element(*MainPage.email1).send_keys("polov12345@yandex.ru")
    driver.find_element(*MainPage.password1).send_keys("123456")
    driver.find_element(*MainPage.authorization).click()
    assert True

# вход через кнопку в форме восстановления пароля
def test_restore_reg_true(driver):
    driver.find_element(*MainPage.cabinet).click()
    driver.find_element(*MainPage.restore).click()
    driver.find_element(*MainPage.entrancesss).click()
    driver.find_element(*MainPage.email1).send_keys("polov12345@yandex.ru")
    driver.find_element(*MainPage.password1).send_keys("123456")
    driver.find_element(*MainPage.authorization).click()
    assert True

# переход в личный кабинет
def test_lk1_true(driver):
    driver.find_element(*MainPage.cabinet).click()
    assert True

# переход из личного кабинета в конструктор
def test_lk_in_designer_true(driver):
    driver.find_element(*MainPage.cabinet).click()
    driver.find_element(*MainPage.designer).click()
    driver.find_element(*MainPage.cabinet).click()
    driver.find_element(*MainPage.logo).click()
    assert True

# переходы к разделам:«Булки»,«Соусы»,«Начинки»
def test_feat_true(driver):
    driver.find_element(*MainPage.sauces).click()
    driver.find_element(*MainPage.fillings).click()
    assert True

# выход из аккаунта
def test_exit_true(driver):
    driver.find_element(*MainPage.cabinet).click()
    driver.find_element(*MainPage.email1).send_keys("polov12345@yandex.ru")
    driver.find_element(*MainPage.password1).send_keys("123456")
    driver.find_element(*MainPage.authorization).click()
    driver.execute_script("arguments[0].click();", *MainPage.cabinet_authorization)
    driver.find_element(*MainPage.exits).click()
    assert True
