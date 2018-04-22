# from tests.conftest import admin_data
# from tests.test_base import TestBase
# from framework.admin_page import AdminPage
#
#
# class TestAdminPage(TestBase):
#
#     def setup_method(self):
#         super().setup_method()
#         self.admin_page = AdminPage(self.driver)
#         self.admin_page.open_admin_page(*admin_data())
#
#     def test_menu_entries(self):
#         # get amount of menu entries
#         amount_of_menu_entries = self.admin_page.get_amount_of_menu_entries()
#         for entry_position in range(1, amount_of_menu_entries + 1):
#             # click on each menu entry
#             self.admin_page.click_on_menu_entry(entry_position)
#             assert self.admin_page.is_headline_displayed(), \
#                 'Headline is displayed on the page number %d' % entry_position
#             amount_of_sub_menu_entries = self.admin_page.get_amount_of_sub_menu_entries()
#             # if sub menu entries exist iterate and click on each sub menu entry
#             if amount_of_sub_menu_entries:
#                 for sub_entry_position in range(1, amount_of_sub_menu_entries + 1) :
#                     self.admin_page.click_on_sub_menu_entry(sub_entry_position)
#                     assert self.admin_page.is_headline_displayed(), \
#                         'Headline is displayed on the sub page number %d' % sub_entry_position
