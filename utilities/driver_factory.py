from selenium import webdriver

# Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Edge
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager

from utilities.logger import Logger
from utilities.config_reader import ConfigReader

logger = Logger.get_logger()


class DriverFactory:

    def __init__(self):
        self.driver = None
        self.config = ConfigReader()

    def get_chrome_options(self):
        options = Options()

        logger.info("Configuring Chrome options.")

        if self.config.is_headless():
            logger.info("Running Chrome in headless mode.")
            options.add_argument("--headless=new")

        options.add_argument("--guest")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")

        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        options.add_experimental_option(
            "prefs",
            {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False
            }
        )

        logger.info("Chrome options configured successfully.")

        return options

    def get_edge_options(self):
        options = EdgeOptions()

        logger.info("Configuring Edge options.")

        options.add_argument("--guest")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")

        logger.info("Edge options configured successfully.")

        return options

    def get_firefox_options(self):
        options = FirefoxOptions()

        logger.info("Configuring Firefox options.")

        # Firefox uses preferences instead of Chrome arguments
        options.set_preference("dom.webnotifications.enabled", False)

        logger.info("Firefox options configured successfully.")

        return options

    def get_driver(self, browser=None):

        browser = self.config.get_browser(browser).lower()

        logger.info(f"Selected browser: {browser}")

        try:

            if browser == "chrome":

                logger.info("Launching Chrome browser.")

                self.driver = webdriver.Chrome(
                    service=Service(ChromeDriverManager().install()),
                    options=self.get_chrome_options()
                )

            elif browser == "edge":

                logger.info("Launching Edge browser.")

                self.driver = webdriver.Edge(
                    service=EdgeService(
                        EdgeChromiumDriverManager().install()
                    ),
                    options=self.get_edge_options()
                )

            elif browser == "firefox":

                logger.info("Launching Firefox browser.")

                self.driver = webdriver.Firefox(
                    service=FirefoxService(
                        GeckoDriverManager().install()
                    ),
                    options=self.get_firefox_options()
                )

            else:
                logger.error(f"Browser '{browser}' is not supported.")
                raise ValueError(f"Browser '{browser}' is not supported.")

            self.driver.maximize_window()
            logger.info(f"{browser.capitalize()} browser launched successfully.")

            return self.driver

        except Exception as e:
            logger.error(f"Failed to launch {browser} browser. Error: {e}")
            raise

    def quit_driver(self):
        if self.driver:
            logger.info("Closing browser.")
            self.driver.quit()
            logger.info("Browser closed successfully.")