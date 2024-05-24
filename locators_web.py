from selenium.webdriver.common.by import By
class MainPage:
# cabinet - переход в личный кабинет
    cabinet = (By.LINK_TEXT, "Личный Кабинет")
# registration -  кнопка зарегистрироваться
    registration = (By.LINK_TEXT, "Зарегистрироваться")
# name - ввод в поле с именем для регистрации
    name = (By.XPATH, ".//body//form//fieldset[1]//input")
# email - ввод в поле с email для регистрации/авторизации
    email1 = (By.XPATH, ".//fieldset[1]//input")
    email = (By.XPATH, ".//fieldset[2]//input")
# password - ввод в поле с паролем для регистрации/авторизации
    password = (By.XPATH, ".//fieldset[3]//input")
    password1 = (By.XPATH, ".//fieldset[2]//input")
# entrance - вход в аккаунт
    entrance = (By.CLASS_NAME, "button_button__33qZ0")
# entrances - переход войти в аккаунт
    entrances = (By.CLASS_NAME, "button_button__33qZ0")
# authorization - кнопка для авторизации
    authorization = (By.CLASS_NAME, "button_button__33qZ0")
# restore - кнопка востановления пароля
    restore = (By.LINK_TEXT, "Восстановить пароль")
# designer - переход в конструктор
    designer = (By.LINK_TEXT, "Конструктор")
# logo - переход на логотип
    logo = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")
# sauces - переход к соусам
    sauces = By.XPATH, ".//section[1]//div[1]"
# fillings - переход к начинкам
    fillings = (By.XPATH, ".//section[1]//div[3]")
# cabinet_authorization - переход в кабинет уже авторизированного пользователя
    cabinet_authorization = (By.LINK_TEXT, "Личный Кабинет")
# exits - выход
    exits = (By.CSS_SELECTOR, '.Account_button__14Yp3')
#entrancesss - вход через востановление
    entrancesss = (By.CLASS_NAME, "Auth_link__1fOlj")
