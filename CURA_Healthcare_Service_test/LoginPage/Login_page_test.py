import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from CURA_Healthcare_Service_test.LoginLocators.login_page_locators import LoginPageLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        enter_username = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(LoginPageLocators.ENTER_USER_NAME))
        enter_username.send_keys(username)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(LoginPageLocators.ENTER_PASSWORD))
        enter_password.send_keys(password)

    def click_login_button(self):
        click_login_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(LoginPageLocators.CLICK_LOGIN_BUTTON))
        click_login_button.click()
        time.sleep(10)


