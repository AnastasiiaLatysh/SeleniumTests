from framework.base_page import BasePage
from framework.locators import CheckoutPageLocators
from selenium.common.exceptions import NoSuchElementException
from helpers.wait import wait_until


class CheckoutPage(BasePage):

    def click_remove_button(self):
        try:
            amount_of_ordered_products_before = self.get_amount_of_ordered_products()
            self.driver.find_element(*CheckoutPageLocators.remove_button).click()
            wait_until(lambda: amount_of_ordered_products_before + 1 == self.get_amount_of_ordered_products())
        except NoSuchElementException:
            pass

    def get_amount_of_ordered_products(self):
        return len(self.find_elements(*CheckoutPageLocators.ordered_products))

    def remove_all_products(self):
        while self.get_amount_of_ordered_products():
            self.click_remove_button()

    def get_empty_cart_message(self):
        return self.driver.find_element(*CheckoutPageLocators.empty_cart_message).text

    def is_empty_cart_message_correct(self, expected_message):
        return wait_until(lambda: self.get_empty_cart_message() == expected_message)
