from framework.home_page import HomePage
from driver.driver import Driver


class TestBase:

    home_page = None
    admin_page = None
    driver = None

    def setup_method(self):
        self.driver = Driver("chrome").get_driver()
        self.home_page = HomePage(self.driver)

    def teardown_method(self):
        self.home_page.quit()
