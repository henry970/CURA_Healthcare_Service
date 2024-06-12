from selenium.webdriver.common.by import By


class LoginPageLocators:
    ENTER_USER_NAME = (By.ID, 'txt-username')
    ENTER_PASSWORD = (By.ID, 'txt-password')
    CLICK_LOGIN_BUTTON = (By.ID, 'btn-login')

