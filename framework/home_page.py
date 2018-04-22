from framework.base_page import BasePage
from selenium.webdriver.common.by import By
from framework.locators import HomePageLocators
from framework.product_page import ProductPage
from framework.checkout_page import CheckoutPage


class HomePage(BasePage):

    def open_product_by_name(self, product_name):
        self.driver.find_element(*HomePageLocators.product_list).find_element(
            By.XPATH, '//a[@title="' + product_name + '"]').click()
        return ProductPage(self.driver)

    def click_cart_checkout(self):
        self.driver.find_element(*HomePageLocators.checkout_link).click()
        return CheckoutPage(self.driver)

    def is_product_list_displayed(self):
        return self.driver.find_element(*HomePageLocators.product_list).is_displayed()
