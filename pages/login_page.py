from lib2to3.pgen2 import driver
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(LoginPageLocators, BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login" in driver.current_url(self.url), "login is absent in current url"
        # реализуйте проверку на корректный url адрес

    def should_be_login_form(self):
        assert self.LOGIN_FORM > 0, "Login link is not presented"
        # реализуйте проверку, что есть форма логина

    def should_be_register_form(self):
        assert self.REGISTRATION_FORM > 0, "Registration link is not presented"
        # реализуйте проверку, что есть форма регистрации на странице


