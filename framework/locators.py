from selenium.webdriver.common.by import By


class AdminPageLocators:
    menu_list = (By.ID, 'box-apps-menu')
    menu_entry = (By.CSS_SELECTOR, 'li[id="app-"]')
    headline = (By.XPATH, '//td[@id="content"]/h1')
    sub_menu_list = (By.XPATH, '//li[@id="app-" and @class="selected"]/ul[@class="docs"]')
    sub_menu_entry = (By.CSS_SELECTOR, 'li[id^="doc"]')


class LoginPageLocators:
    login_form = (By.NAME, 'login_form')
    username_field = (By.NAME, 'username')
    password_field = (By.NAME, 'password')
    login_button = (By.NAME, 'login')
    logout_link = (By.CSS_SELECTOR, 'a[title="Logout"]')
