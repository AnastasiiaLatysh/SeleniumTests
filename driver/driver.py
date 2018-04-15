from selenium import webdriver
from configs.configs import Configs


class Driver:
    def __init__(self, driver_name):
        if driver_name == 'chrome':
            self.driver = webdriver.Chrome(Configs.path_to_chrome_driver)

    def get_driver(self):
        return self.driver
