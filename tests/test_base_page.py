from tests.test_base import BaseTest


class TestBasePage(BaseTest):

    def test_title(self):
        assert self.base_page.get_title() == 'Online Store | My Store'
