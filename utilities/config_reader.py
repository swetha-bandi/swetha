import configparser
import os


class ConfigReader:
    """
    Reads values from config.ini
    """

    def __init__(self):
        self.config = configparser.ConfigParser()

        config_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "config",
            "config.ini"
        )

        self.config.read(config_path)

    def get_browser(self, browser=None):
        if browser:
            return browser
        return self.config["DEFAULT"]["browser"]

    def get_url(self, env=None):
        if env:
            environment = env.upper()
        else:
            environment = self.config["DEFAULT"]["environment"].upper()

        return self.config[environment]["url"]

    def get_implicit_wait(self):
        return int(self.config["DEFAULT"]["implicit_wait"])

    def get_explicit_wait(self):
        return int(self.config["DEFAULT"]["explicit_wait"])

    def is_headless(self):
        return self.config["DEFAULT"].getboolean("headless")