from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

from utilities.waits import WaitUtils
from utilities.config_reader import ConfigReader
from utilities.logger import Logger


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.config = ConfigReader()
        self.logger = Logger.get_logger()
        self.wait = WaitUtils(self.driver)

    def click(self, locator):
        self.logger.info(f"Clicking element: {locator}")

        try:
            element = self.wait.wait_until_clickable(locator)
            element.click()

        except Exception as e:
            self.logger.error(f"Failed to click element: {locator}. Error:{e}")
            raise


    def enter_text(self, locator, text):
        self.logger.info(f"Entering text into element: {locator}")

        try:
            element = self.wait.wait_until_visible(locator)
            element.clear()
            element.send_keys(text)

        except Exception as e:
            self.logger.error(f"Failed to enter text into element: {locator}. Error: {e}")
            raise


    def get_text(self, locator):
        self.logger.info(f"Getting text from element: {locator}")

        try:
            return self.wait.wait_until_visible(locator).text
        except Exception as e:
            self.logger.error(f"Failed to get text from element: {locator}. Error: {e}")
            raise


    def is_displayed(self, locator):
        self.logger.info(f"Checking visibility of element: {locator}")

        try:
            return self.wait.wait_until_visible(locator).is_displayed()
        except Exception as e:
            self.logger.error(f"Failed to verify display status of element: {locator}. Error: {e}")
            raise


    def select(self, locator):
        self.logger.info(f"Selecting element: {locator}")

        try:
            element = self.wait.wait_until_visible(locator)
            if not element.is_selected():
                   element.click()
        except Exception as e:
            self.logger.error(f"Failed to select element: {locator}. Error: {e}")
            raise

    def check(self, locator):
        self.logger.info(f"Checking element: {locator}")

        try:
            element = self.wait.wait_until_clickable(locator)

            if not element.is_selected():
                element.click()

        except Exception as e:
            self.logger.error(f"Failed to check element: {locator}. Error: {e}")
            raise

    def uncheck(self, locator):
        self.logger.info(f"Unchecking element: {locator}")

        try:
            element = self.wait.wait_until_visible(locator)
            if element.is_selected():
               element.click()
        except Exception as e:
            self.logger.error(f"Failed to uncheck element: {locator}. Error: {e}")
            raise


    def select_by_text(self, locator, text):
        self.logger.info(f"Selecting '{text}' from dropdown.")

        try:
            element = self.wait.wait_until_clickable(locator)
            Select(element).select_by_visible_text(text)
        except Exception as e:
            self.logger.error(
                f"Failed to select '{text}' from dropdown: {locator}. Error: {e}"
            )
            raise


    def move_to_element(self, locator):
        self.logger.info(f"Hovering over element: {locator}")

        try:
            element = self.wait.wait_until_visible(locator)
            ActionChains(self.driver).move_to_element(element).perform()
        except Exception as e:
            self.logger.error(f"Failed to hover over element: {locator}. Error: {e}")
            raise



