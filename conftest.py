import pytest
from utilities.driver_factory import DriverFactory
from utilities.config_reader import ConfigReader
from utilities.screenshots import Screenshot
from utilities.excel_reader import ExcelReader
from utilities.logger import Logger
import allure

@pytest.fixture(scope="session")
def login_test_data():
    return ExcelReader.get_data(
        "login_data.xlsx",
        "Login"
    )

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        if report.failed:
            if "driver" in item.funcargs:
                driver = item.funcargs["driver"]
                Screenshot.take_screenshot(driver, item.name)

                allure.attach.file(
                    Logger.get_log_file(),
                    name="Execution Logs",
                    attachment_type=allure.attachment_type.TEXT
                )


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser")
    env = request.config.getoption("--env")

    factory = DriverFactory()
    browser = factory.get_driver(browser_name)

    config = ConfigReader()
    browser.get(config.get_url(env))

    try:
        yield browser
    finally:
        browser.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default=None,
        help="Browser to execute tests"
    )

    parser.addoption(
        "--env",
        action="store",
        default=None,
        help="Environment to execute tests"
    )


