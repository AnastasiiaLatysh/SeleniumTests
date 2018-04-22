from framework.base_page import BasePage
from framework.locators import AddNewProductPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from framework.expected_conditions import element_has_correct_image_path
from selenium.webdriver.support.ui import Select


class AddNewProductPage(BasePage):
    def __init__(self, driver):
        super(AddNewProductPage, self).__init__(driver)

    def open_general_tab(self):
        self.driver.find_element(*AddNewProductPageLocators.general_tab).click()

    def open_prices_tab(self):
        self.driver.find_element(*AddNewProductPageLocators.prices_tab).click()

    def is_general_tab_opened(self):
        return self.is_element_clickable(AddNewProductPageLocators.general_tab_content)

    def is_prices_tab_opened(self):
        return self.is_element_clickable(AddNewProductPageLocators.prices_tab_content)

    def enter_price(self, purchase_price):
        self.driver.find_element(*AddNewProductPageLocators.purchase_price).send_keys(purchase_price)

    def is_price_entered(self, purchase_price):
        return self.is_text_present_in_element_value(AddNewProductPageLocators.purchase_price, str(purchase_price))

    def make_status_enabled(self):
        self.is_element_present(AddNewProductPageLocators.status_entry_enabled)
        if not self.driver.find_element(*AddNewProductPageLocators.status_entry_enabled).is_selected():
            self.driver.find_element(*AddNewProductPageLocators.status_entry_enabled).click()

    def is_product_status_enabled(self):
        return self.is_element_selected(AddNewProductPageLocators.status_entry_enabled)

    def enter_product_name(self, product_name):
        self.driver.find_element(*AddNewProductPageLocators.product_name).send_keys(product_name)

    def is_product_name_entered(self, product_name):
        return self.is_text_present_in_element_value(AddNewProductPageLocators.product_name, product_name)

    def check_product_group_unisex(self):
        if not self.driver.find_element(*AddNewProductPageLocators.product_group_unisex).is_selected():
            self.driver.find_element(*AddNewProductPageLocators.product_group_unisex).click()

    def is_unisex_group_selected(self):
        return self.is_element_selected(AddNewProductPageLocators.product_group_unisex)

    def set_product_quantity(self, product_quantity):
        self.driver.find_element(*AddNewProductPageLocators.product_quantity).send_keys(product_quantity)

    def is_product_quantity_set(self, product_quantity):
        return self.is_text_present_in_element_value(AddNewProductPageLocators.product_quantity, str(product_quantity))

    def upload_product_image(self, path_to_image):
        self.driver.find_element(*AddNewProductPageLocators.upload_product_image).send_keys(path_to_image)
        WebDriverWait(self.driver, 10).until(element_has_correct_image_path(
            AddNewProductPageLocators.upload_product_image, path_to_image))

    def save_new_product(self):
        self.driver.find_element(*AddNewProductPageLocators.save_product).click()

    def is_success_notice_appeared(self):
        return self.is_element_present(AddNewProductPageLocators.notice_success)

    def select_purchase_currency(self, currency_code='EUR'):
        purchase_currency_select = Select(self.driver.find_element(*AddNewProductPageLocators.purchase_currency))
        purchase_currency_select.select_by_value(currency_code)
