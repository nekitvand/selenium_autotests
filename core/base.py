from dataclasses import dataclass
from selenium.webdriver.common.by import By
from helpers.find_actions import FindAction
from helpers.element_actions import ElementAction
from helpers.url_actions import UrlAction
from helpers.alert_actions import AlertAction
from helpers.action_chains import ActionChain
from helpers.cookies_actions import CookiesAction
from helpers.css_actions import CssAction
from helpers.keys_actions import KeysAction
from helpers.execute_script_actions import ExecuteScript
from helpers.select_actions import SelectAction


@dataclass()
class Locators:
    CSS_SELECTOR: str = By.CSS_SELECTOR
    XPATH: str = By.XPATH
    CLASS_NAME: str = By.CLASS_NAME
    LINK_TEXT: str = By.LINK_TEXT


class Base:

    def __init__(self, driver):
        self.driver = driver
        self.FindAction = FindAction(driver)
        self.ElementAction = ElementAction(driver)
        self.UrlAction = UrlAction(driver)
        self.AlertAction = AlertAction(driver)
        self.ActionChain = ActionChain(driver)
        self.CookiesAction = CookiesAction(driver)
        self.CssAction = CssAction()
        self.KeysAction = KeysAction()
        self.ExecuteScript = ExecuteScript(driver)
        self.SelectAction = SelectAction(driver)


