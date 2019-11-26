from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, 'word "login" not in url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM)

    def register_new_user(self, email, password):
        element_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        element_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        element_confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRMATION_PASSWORD)
        element_email.send_keys(email)
        element_password.send_keys(password)
        element_confirm_password.send_keys(password)
        button_register = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        button_register.click()

