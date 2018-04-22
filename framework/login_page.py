from framework.base_page import BasePage
from framework.locators import LoginPageLocators


class LoginPage(BasePage):

    def enter_username(self, username):
        self.driver.find_element(*LoginPageLocators.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*LoginPageLocators.password_field).send_keys(password)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.driver.find_element(*LoginPageLocators.login_button).click()

    def is_user_logged_in(self):
        return self.is_element_present(LoginPageLocators.logout_link)
