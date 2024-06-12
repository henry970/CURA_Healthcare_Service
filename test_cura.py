import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from CURA_Healthcare_Service_test.LoginPage.Login_page_test import LoginPage
from CURA_Healthcare_Service_test.AppointmentPage.appointment_page_test import AppointmentPage


#
@pytest.fixture(scope="module")
def driver_setup():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.implicitly_wait(20)
    yield driver
    driver.quit()


# @pytest.fixture(scope="module")
# def driver_setup():
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(30)
#     driver.maximize_window()
#     yield driver
#     driver.quit()


@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.login_url("https://katalon-demo-cura.herokuapp.com/profile.php#login")
    return login_page


def test_login_to_CURA_Healthcare_service(login):
    login.enter_username("John Doe")
    login.enter_password("ThisIsNotAPassword")
    login.click_login_button()


def Book_appointment_for_CURA_Healthcare_service(login):
    fill_appointment_form = AppointmentPage(login.driver)
    fill_appointment_form.check_apply_hospital_button()
    fill_appointment_form.click_visit_date_field()
    fill_appointment_form.select_visit_date()
    fill_appointment_form.enter_comment("Test_Automation")
    fill_appointment_form.click_appointment_button()
