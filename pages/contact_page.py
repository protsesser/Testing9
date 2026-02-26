from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ContactPage(BasePage):

    NAME = (By.ID, "name")
    EMAIL = (By.ID, "email")
    SUBJECT = (By.ID, "subject")
    MESSAGE = (By.ID, "message")
    SUBMIT = (By.ID, "submitBtn")

    NAME_ERROR = (By.ID, "nameError")
    EMAIL_ERROR = (By.ID, "emailError")
    MESSAGE_ERROR = (By.ID, "messageError")
    SUCCESS = (By.ID, "successMessage")

    def fill_name(self, name):
        self.type(self.NAME, name)

    def fill_email(self, email):
        self.type(self.EMAIL, email)

    def fill_subject(self, subject):
        self.type(self.SUBJECT, subject)

    def fill_message(self, message):
        self.type(self.MESSAGE, message)

    def submit(self):
        self.click(self.SUBMIT)

    def is_success_displayed(self):
        return self.find(self.SUCCESS).is_displayed()

    def is_name_error_displayed(self):
        return self.find(self.NAME_ERROR).is_displayed()

    def is_email_error_displayed(self):
        return self.find(self.EMAIL_ERROR).is_displayed()

    def is_message_error_displayed(self):
        return self.find(self.MESSAGE_ERROR).is_displayed()