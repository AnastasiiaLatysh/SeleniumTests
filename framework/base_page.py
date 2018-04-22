import time
from configs.config import Config
from framework.locators import HomePageLocators, AdminPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from framework.expected_conditions import element_has_attribute_with_value


class BasePage(object):

    base_url = Config.base_url
    driver = None

    def __init__(self, driver, url=base_url):
        self.driver = driver
        self.url = url

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def open(self, url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()

    def find_elements(self, *locators, time_to_load=15, time_to_wait_between_comparison=1):
        start_time = time.time()
        end_time = start_time + time_to_load
        while time.time() < end_time:
            try:
                self.is_element_present(locators, timeout=2)
                entries_before = self.driver.find_elements(*locators)
                time.sleep(time_to_wait_between_comparison)
                entries_after = self.driver.find_elements(*locators)
                if entries_before == entries_after:
                    return entries_before
            except TimeoutException:
                return []

    def get_amount_of_products_in_cart(self):
        return int(self.driver.find_element(*HomePageLocators.cart).find_element(*HomePageLocators.cart_quantity).text)

    def is_headline_correct(self, expected_headline):
        return self.driver.find_element(*AdminPageLocators.headline).text == expected_headline

    def is_element_present(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_element_clickable(self, locator, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator))
        except TimeoutException:
            return False

    def is_element_contain_attribute_with_value(self, locator, attribute_name, attribute_value, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(
                element_has_attribute_with_value(locator, attribute_name, attribute_value))
        except TimeoutException:
            return False

    def is_text_present_in_element_value(self, locator, expected_text, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.text_to_be_present_in_element_value(locator, expected_text))
        except TimeoutException:
            return False

    def is_element_selected(self, locator, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.element_located_to_be_selected(locator))
        except TimeoutException:
            return False
