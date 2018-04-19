from selenium import webdriver
from configs.config import Config


class Driver:
    def __init__(self, driver_name):
        if driver_name == 'chrome':
            self.driver = webdriver.Chrome(Config.path_to_chrome_driver)

    def get_driver(self):
        return self.driver
