from driver.driver import Driver


class BasePage:
    def __init__(self, driver_name, url):
        self.driver = Driver(driver_name).get_driver()
        self.url = url

    def get_title(self):
        return self.driver.title

    def open_home_page(self):
        self.driver.get(self.url)

    def quit(self):
        self.driver.quit()
