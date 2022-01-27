import pytest
import os
import json
from selenium import webdriver


def determine_scope(fixture_name, config):
    if config.getoption("--reload", True):
        return "function"
    return "session"


def pytest_addoption(parser):
    parser.addoption('--browser', action="store", default="chrome")
    parser.addoption('--remote_url', action="store", default='http://localhost:4444/wd/hub')


@pytest.fixture(scope=determine_scope)
def params_builder(request):
    config_params = {"browser": request.config.getoption('--browser'),
                     "remote_url": request.config.getoption("--remote_url")}
    return config_params


class Browser:

    def __init__(self, config):
        self.config = config
        self.name = self.config.get("browser")
        self.version = None

    def get_selenoid_json_config(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/config/browsers.json"
        with open(path, "r") as file:
            config = json.load(file)
        return config

    def get_version_browser(self):
        selenoid_config = self.get_selenoid_json_config()
        self.version = selenoid_config[self.name]["default"]
        return None

    def remote_browser(self, ):
        self.get_version_browser()
        capabilities = {
            "browserName": f"{self.name}",
            "browserVersion": f"{self.version}",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False
            }
        }
        driver = webdriver.Remote(
            command_executor=self.config["remote_url"], desired_capabilities=capabilities)
        driver.set_window_size(1920, 1080)
        return driver


@pytest.fixture(scope=determine_scope)
def browser(params_builder):
    driver = Browser(params_builder).remote_browser()
    driver.get("https://habr.com/ru")
    yield driver
    driver.close()
    driver.quit()
