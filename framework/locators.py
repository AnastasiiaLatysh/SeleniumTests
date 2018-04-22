from selenium.webdriver.common.by import By


class HomePageLocators:
    product_list = (By.XPATH, '//ul[@class="listing-wrapper products"]')
    cart = (By.XPATH, '//div[@id="cart"]')
    cart_quantity = (By.XPATH, '//span[@class="quantity"]')
    checkout_link = (By.XPATH, '//a[contains(@href, "checkout")]')


class ProductPageLocators:
    product_info = (By.XPATH, '//div[@id="box-product"]')
    add_to_cart = (By.XPATH, '//button[@name="add_cart_product"]')


class CheckoutPageLocators:
    remove_button = (By.XPATH, '//button[@name="remove_cart_item"]')
    order_information = (By.XPATH, '//div[@id="order_confirmation-wrapper"]')
    ordered_products = (By.XPATH, '//tr/td[@class="item"]')
    empty_cart_message = (By.XPATH, '//div[@id="checkout-cart-wrapper"]/p/em')


class AdminPageLocators:
    menu_list = (By.ID, 'box-apps-menu')
    menu_entry = (By.CSS_SELECTOR, 'li[id="app-"]')
    headline = (By.XPATH, '//td[@id="content"]/h1')
    sub_menu_list = (By.XPATH, '//li[@id="app-" and @class="selected"]/ul[@class="docs"]')
    sub_menu_entry = (By.CSS_SELECTOR, 'li[id^="doc"]')
    catalog_menu_entry = (By.XPATH, '//a[contains(@href,"catalog")]')
    catalog_sub_menu_entry = (By.XPATH, '//li[@id="doc-catalog"]')


class CatalogPageLocators:
    add_new_product_button = (By.XPATH, '//a[contains(@href, "doc=edit_product")]')
    added_products = (By.XPATH, '//table[@class="dataTable"]/tbody/tr[@class="row"]')


class AddNewProductPageLocators:
    tabs = (By.XPATH, '//div[@class="tabs"]')
    general_tab = (By.XPATH, '//a[@href="#tab-general"]')
    general_tab_content = (By.XPATH, '//div[@id="tab-general"]')
    prices_tab_content = (By.XPATH, '//div[@id="tab-prices"]')
    prices_tab = (By.XPATH, '//a[@href="#tab-prices"]')
    status_entry_enabled = (By.XPATH, '//input[@name="status" and @type="radio" and @value="1"]')
    product_name = (By.XPATH, '//input[contains(@name, "name") and @type="text"]')
    product_group_unisex = (By.XPATH, '//input[@name, "product_groups[]" and @value="1-3" and @type="checkbox"]')
    product_quantity = (By.XPATH, '//input[@name="quantity" and @type="number"]')
    upload_product_image = (By.XPATH, '//input[@type="file"]')
    save_product = (By.XPATH, '//button[@type="submit" and @name="save"]')
    notice_success = (By.XPATH, '//div[@class="notice success"]')
    purchase_price = (By.XPATH, '//input[@name="purchase_price"]')
    purchase_currency = (By.XPATH, '//select[@name="purchase_price_currency_code"]')


class LoginPageLocators:
    login_form = (By.NAME, 'login_form')
    username_field = (By.NAME, 'username')
    password_field = (By.NAME, 'password')
    login_button = (By.NAME, 'login')
    logout_link = (By.CSS_SELECTOR, 'a[title="Logout"]')
