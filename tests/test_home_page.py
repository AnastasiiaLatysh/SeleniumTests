from tests.test_base import TestBase
from framework.admin_page import AdminPage
from tests.conftest import admin_data, get_empty_cart_message, get_add_new_product_headline, get_home_title
import os
from helpers.data_generation import generate_random_string_with_digits, generate_random_integer


class TestHomePage(TestBase):

    def setup_method(self):
        super().setup_method()
        self.home_page.open(self.home_page.base_url)
        self.admin_page = AdminPage(self.driver)

    def test_title(self):
        assert self.home_page.get_title() == get_home_title(), 'Home page title is correct'

    def test_add_and_remove_product(self):
        # 1. Open admin page (data is used for login)
        self.admin_page.open_admin_page(*admin_data())
        assert 'ammin' in self.admin_page.get_current_url(), 'Admin page is opened'

        # 2. Open catalog
        catalog_page = self.admin_page.open_catalog_menu()
        assert self.admin_page.is_catalog_menu_entry_selected(), 'Catalog menu entry is selected on the left side menu'
        # save amount of products before adding new one
        amount_of_products_before = catalog_page.get_amount_of_products()

        # 3. Click 'Add new product' button and fill necessary field
        add_new_product_page = catalog_page.click_add_new_product_button()
        assert add_new_product_page.is_headline_correct(get_add_new_product_headline())

        # 3.1. Open general tab and fill info
        add_new_product_page.open_general_tab()
        assert add_new_product_page.is_general_tab_opened(), 'General tab is opened'
        add_new_product_page.make_status_enabled()
        assert add_new_product_page.is_product_status_enabled(), 'Product status is enabled'
        product_name = generate_random_string_with_digits()
        add_new_product_page.enter_product_name(product_name)
        assert add_new_product_page.is_product_name_entered(product_name)
        quantity = generate_random_integer()
        add_new_product_page.set_product_quantity(quantity)
        assert add_new_product_page.is_product_quantity_set(quantity)
        add_new_product_page.upload_product_image(os.getcwd() + "/tests/my_product.png")

        # 3.2. Open prices tab and fill price
        add_new_product_page.open_prices_tab()
        assert add_new_product_page.is_prices_tab_opened(), 'Prices tab is opened'
        price = generate_random_integer()
        add_new_product_page.enter_price(price)
        assert add_new_product_page.is_price_entered(price), 'Price is enetered'
        add_new_product_page.select_purchase_currency('EUR')

        # 3.3. Save product
        add_new_product_page.save_new_product()
        assert amount_of_products_before + 1 == catalog_page.get_amount_of_products(), 'Product was added'

        # 4. Open main page
        self.home_page.open(self.home_page.base_url)
        assert self.home_page.is_product_list_displayed(), 'Product list is displayed'

        # 5. Click on product which was recently added and add it to the cart
        product_page = self.home_page.open_product_by_name(product_name)
        assert product_page.is_opened(), 'Product page is opened'
        product_page.click_add_to_cart()

        # 6. Click checkout and remove all products from cart
        checkout_page = self.home_page.click_cart_checkout()
        checkout_page.remove_all_products()
        assert checkout_page.is_empty_cart_message_correct(get_empty_cart_message()), \
            'Message that cart is empty is correct'
