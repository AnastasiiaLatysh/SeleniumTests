from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging
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
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LoginPageLocators.logout_link))
        except TimeoutException:
            logging.error("Unable to find logout link to identify if user is logged in")
