from selenium.webdriver.common.by import By


class AppointmentPageLocators:
    CHECK_APPLY_HOSPITAL = (By.ID, "chk_hospotal_readmission")
    CLICK_VISIT_DATE_FIELD = (By.ID, "txt_visit_date")
    SELECT_VISIT_DATE = (By.XPATH, '/html/body/div/div[1]/table/tbody/tr[4]/td[4]')
    ENTER_COMMENT = (By.ID, "txt_comment")
    CLICK_BOOK_APPOINTMENT = (By.ID, "btn-book-appointment")
