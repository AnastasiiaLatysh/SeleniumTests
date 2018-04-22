from framework.base_page import BasePage
from framework.locators import ProductPageLocators, HomePageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):

    def is_opened(self):
        return self.is_element_clickable(ProductPageLocators.product_info)

    def click_add_to_cart(self):
        amount_before = self.get_amount_of_products_in_cart()
        self.driver.find_element(*ProductPageLocators.add_to_cart).click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(
            HomePageLocators.cart_quantity, str(amount_before + 1)))
