from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from CURA_Healthcare_Service_test.AppointmentPageLocators.appointment_page_locators_test import AppointmentPageLocators


class AppointmentPage:
    def __init__(self, driver):
        self.driver = driver

    def check_apply_hospital_button(self):
        check_apply_hospital_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(AppointmentPageLocators.CHECK_APPLY_HOSPITAL))
        check_apply_hospital_button.click()

    def click_visit_date_field(self):
        click_visit_date_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(AppointmentPageLocators.CLICK_VISIT_DATE_FIELD))
        click_visit_date_field.click()

    def select_visit_date(self):
        select_visit_date_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(AppointmentPageLocators.SELECT_VISIT_DATE))
        select_visit_date_field.click()

    def enter_comment(self, comment):
        enter_comment = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(AppointmentPageLocators.ENTER_COMMENT))
        enter_comment.send_keys(comment)

    def click_appointment_button(self):
        click_appointment_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(AppointmentPageLocators.CLICK_BOOK_APPOINTMENT))
        click_appointment_button.click()

