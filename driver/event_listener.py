from selenium.webdriver.support.event_firing_webdriver import AbstractEventListener
import logging
import os
import sys


class EventListener(AbstractEventListener):

    def before_navigate_to(self, url, driver):
        logging.log(90, "Before navigating to page with url: %s" % url)

    def after_navigate_to(self, url, driver):
        logging.log(90, "After navigating from page with url: %s" % url)

    def before_navigate_back(self, driver):
        logging.log(90, "Before navigating back")

    def after_navigate_back(self, driver):
        logging.log(90, "After navigating back")

    def before_navigate_forward(self, driver):
        logging.log(90, "Before navigating forward")

    def after_navigate_forward(self, driver):
        logging.log(90, "After navigating forward")

    def before_find(self, by, value, driver):
        logging.log(90, "Before find element with value: %s, by locator: %s" % (value, by))

    def after_find(self, by, value, driver):
        logging.log(90, "After find element with value: %s, by locator: %s" % (value, by))

    def before_click(self, element, driver):
        logging.log(90, "Before click on element %s" % element)

    def after_click(self, element, driver):
        logging.log(90, "After click on element %s" % element)

    def before_change_value_of(self, element, driver):
        logging.log(90, "Before change value of element %s" % element)

    def after_change_value_of(self, element, driver):
        logging.log(90, "After change value of element %s" % element)

    def before_execute_script(self, script, driver):
        logging.log(90, "Before execute script")

    def after_execute_script(self, script, driver):
        logging.log(90, "After execute script")

    def before_close(self, driver):
        logging.log(90, "Before closing")

    def after_close(self, driver):
        logging.log(90, "After closing")

    def before_quit(self, driver):
        logging.log(90, "Before quiting")

    def after_quit(self, driver):
        logging.log(90, "After quiting")

    def on_exception(self, exception, driver):
        logging.log(90, "Before execution after exception occurred")
        # make screen shot of fail
        test_class_and_method_name = type(self).__name__
        print(os.getcwd())
        driver.get_screenshot_as_file(os.getcwd() + "/screenshots/Screenshots%s_%s.png" %
                                      test_class_and_method_name)
