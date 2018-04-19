from configs.config import Config


class BasePage:

    base_url = Config.base_url
    driver = None

    def __init__(self, driver, url=base_url):
        self.driver = driver
        self.url = url

    def get_title(self):
        return self.driver.title

    def open(self, url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()
