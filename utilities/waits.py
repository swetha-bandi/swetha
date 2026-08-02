from selenium.webdriver.support.wait import WebDriverWait
from utilities.config_reader import ConfigReader
from selenium.webdriver.support import expected_conditions as EC


class WaitUtils:

    def __init__(self, driver):
        self.driver = driver

        config = ConfigReader()
        self.timeout = config.get_explicit_wait()

        self.wait = WebDriverWait(self.driver, self.timeout)

    def wait_until_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_until_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

