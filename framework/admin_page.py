from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from framework.base_page import BasePage
from framework.locators import AdminPageLocators
from framework.login_page import LoginPage
from selenium.webdriver.common.by import By


class AdminPage(BasePage):
    def __init__(self, driver):
        self.url = super().base_url + '/admin'
        super(AdminPage, self).__init__(driver, self.url)

    def open_admin_page(self, admin_name='', admin_password=''):
        self.driver.get(self.url)
        if 'login' in self.driver.current_url:
            LoginPage(self.driver).login(admin_name, admin_password)

    def get_amount_of_menu_entries(self):
        menu_entries = self.driver.find_element(*AdminPageLocators.menu_list).find_elements(
            *AdminPageLocators.menu_entry)
        return len(menu_entries)

    def get_amount_of_sub_menu_entries(self):
        try:
            sub_menu_entries = self.driver.find_element(*AdminPageLocators.sub_menu_list).find_elements(
                *AdminPageLocators.sub_menu_entry)
            return len(sub_menu_entries)
        except NoSuchElementException:
            return 0

    def click_on_menu_entry(self, menu_entry_index):
        self.driver.find_element(*AdminPageLocators.menu_list).find_element(
            By.CSS_SELECTOR, 'li[id="app-"]:nth-child(' + str(menu_entry_index) + ')').click()

    def click_on_sub_menu_entry(self, sub_menu_entry_index):
        self.driver.find_element(*AdminPageLocators.sub_menu_list).find_element(
            By.CSS_SELECTOR, 'li[id^="doc"]:nth-child(' + str(sub_menu_entry_index) + ')').click()

    def is_headline_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(AdminPageLocators.headline))
            return True
        except TimeoutException:
            return False
