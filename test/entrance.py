from locators_web import *
from conftest import *

# ошибка с неккоректным паролем
def test_registration_form_no_correctly_true(driver):
    driver.find_element(*MainPage.cabinet).click()
    driver.find_element(*MainPage.registration).click()
    driver.find_element(*MainPage.name).send_keys("Анастасия")
    driver.find_element(*MainPage.email).send_keys("polovnikova123@yandex.ru")
    driver.find_element(*MainPage.password).send_keys("12345")
    driver.find_element(*MainPage.entrance).click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

# успешная регистрация
def test_registration_form_true(driver):
    driver.find_element(*MainPage.cabinet).click()
    driver.find_element(*MainPage.registration).click()
    driver.find_element(*MainPage.name).send_keys("Анастасия")
    driver.find_element(*MainPage.email).send_keys("polovnnnn1ikova123@yandex.ru")
    driver.find_element(*MainPage.password).send_keys("123456")
    driver.find_element(*MainPage.entrance).click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

# вход по кнопке «Войти в аккаунт» на главной
def test_entrances_true(driver):
    driver.find_element(*MainPage.entrances).click()
    driver.find_element(*MainPage.email1).send_keys("polov12345@yandex.ru")
    driver.find_element(*MainPage.password1).send_keys("123456")
    driver.find_element(*MainPage.authorization).click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

# вход через кнопку «Личный кабинет»
def test_lk_true(driver):
    driver.find_element(*MainPage.cabinet).click()
    driver.find_element(*MainPage.email1).send_keys("polov12345@yandex.ru")
    driver.find_element(*MainPage.password1).send_keys("123456")
    driver.find_element(*MainPage.authorization).click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

# вход через кнопку в форме регистрации
def test_etrances_reg_true(driver):
    driver.find_element(*MainPage.cabinet).click()
    driver.find_element(*MainPage.registration).click()
    driver.find_element(*MainPage.entrances).click()
    driver.find_element(*MainPage.email1).send_keys("polov12345@yandex.ru")
    driver.find_element(*MainPage.password1).send_keys("123456")
    driver.find_element(*MainPage.authorization).click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

# вход через кнопку в форме восстановления пароля
def test_restore_reg_true(driver):
    driver.find_element(*MainPage.cabinet).click()
    driver.find_element(*MainPage.restore).click()
    driver.find_element(*MainPage.entrancesss).click()
    driver.find_element(*MainPage.email1).send_keys("polov12345@yandex.ru")
    driver.find_element(*MainPage.password1).send_keys("123456")
    driver.find_element(*MainPage.authorization).click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

# переход в личный кабинет
def test_lk1_true(driver):
    driver.find_element(MainPage.cabinet).click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

# переход из личного кабинета в конструктор
def test_lk_in_designer_true(driver):
    driver.find_element(*MainPage.cabinet).click()
    driver.find_element(*MainPage.designer).click()
    driver.find_element(*MainPage.cabinet).click()
    driver.find_element(*MainPage.logo).click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

# переходы к разделам:«Булки»,«Соусы»,«Начинки»
def test_feat_true(driver):
    driver.find_element(*MainPage.sauces).click()
    driver.find_element(*MainPage.fillings).click()
    assert MainPage.fillings.text == 'Начинки'

# выход из аккаунта
def test_exit_true(driver):
    driver.find_element(*MainPage.cabinet).click()
    driver.find_element(*MainPage.email1).send_keys("polov12345@yandex.ru")
    driver.find_element(*MainPage.password1).send_keys("123456")
    driver.find_element(*MainPage.authorization).click()
    driver.execute_script("arguments[0].click();", *MainPage.cabinet_authorization)
    driver.find_element(*MainPage.exits).click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
