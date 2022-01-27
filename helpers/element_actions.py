from typing import List
from typing import Tuple
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class ElementAction:

    def __init__(self, driver):
        self.driver = driver
        self.test_url = None

    def get_attribute_by_element(self, element, name):
        return element.get_attribute(name)

    def scroll_to_element(self, element):
        return element.location_once_scrolled_into_view

    @classmethod
    def click(cls, element):
        element.click()

    @classmethod
    def send(cls, web_element, text):
        web_element.clear()
        web_element.send_keys(text)

    @classmethod
    def get_text(cls, element):
        return element.text

    @classmethod
    def get_text_content(cls, element):
        return element.get_attribute('textContent')