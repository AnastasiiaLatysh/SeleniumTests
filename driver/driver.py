from selenium import webdriver
from configs.config import Config
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from driver.event_listener import EventListener


class Driver:
    def __init__(self, driver_name):
        if driver_name == 'chrome':
            self.driver = EventFiringWebDriver(webdriver.Chrome(Config.path_to_chrome_driver),
                                               EventListener())

    def get_driver(self):
        return self.driver
