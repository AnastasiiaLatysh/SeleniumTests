from framework.base_page import BasePage
from configs.configs import Configs


class BaseTest:

    base_page = None

    @classmethod
    def setup_class(cls):
        cls.base_page = BasePage('chrome', Configs.base_url)
        cls.base_page.open_home_page()

    @classmethod
    def teardown_class(cls):
        cls.base_page.quit()
