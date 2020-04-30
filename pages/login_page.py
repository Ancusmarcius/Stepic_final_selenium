from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        input_mail = self.browser.find_element(*LoginPageLocators.REG_MAIL)
        input_mail.send_keys(email)
        input_pass1 = self.browser.find_element(*LoginPageLocators.REG_PASS1)
        input_pass1.send_keys(password)
        input_pass2 = self.browser.find_element(*LoginPageLocators.REG_PASS2)
        input_pass2.send_keys(password)
        btn_accept = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        btn_accept.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "в адресе отсутствует login"

    def should_be_login_form(self):

        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM) and\
               self.is_element_present(*LoginPageLocators.LOGIN_MAIL) and\
               self.is_element_present(*LoginPageLocators.LOGIN_PASS), "проблеммы с формой логина"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM) and\
               self.is_element_present(*LoginPageLocators.REG_MAIL) and\
               self.is_element_present(*LoginPageLocators.REG_PASS1) and\
               self.is_element_present(*LoginPageLocators.REG_PASS2), "проблемы с формой регистрации"
