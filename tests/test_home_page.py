from tests.test_base import TestBase


class TestHomePage(TestBase):

    def setup_method(self):
        super().setup_method()
        self.home_page.open(self.home_page.base_url)

    def test_title(self):
        assert self.home_page.get_title() == 'Online Store | My Store', 'Home page title is correct'
