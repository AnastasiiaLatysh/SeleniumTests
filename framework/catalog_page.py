from framework.base_page import BasePage
from framework.locators import CatalogPageLocators, AdminPageLocators
from framework.add_new_product_page import AddNewProductPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CatalogPage(BasePage):

    def __init__(self, driver):
        super(CatalogPage, self).__init__(driver)

    def click_add_new_product_button(self):
        self.driver.find_element(*CatalogPageLocators.add_new_product_button).click()
        return AddNewProductPage(self.driver)

    def get_amount_of_products(self):
        return len(self.find_elements(*CatalogPageLocators.added_products))
