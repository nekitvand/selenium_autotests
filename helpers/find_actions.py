from typing import List
from typing import Tuple
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FindAction:

    def __init__(self, driver):
        self.driver = driver
        self.test_url = None

    def find(self, locator, timeout=10):
        """Поиск и ожидание единственного элемента"""
        return WebDriverWait(self.driver, timeout, poll_frequency=1). \
            until(EC.presence_of_element_located(locator))

    def find_visible(self, locator, timeout=10):
        """Поиск и ожидание единственного видимого элемента """
        return WebDriverWait(self.driver, timeout, poll_frequency=1). \
            until(EC.visibility_of_element_located(locator))

    def finds(self, locator, timeout=10):
        """Поиск и ожидание нескольких элементов"""
        return WebDriverWait(self.driver, timeout, poll_frequency=1). \
            until(EC.presence_of_all_elements_located(locator))

    def finds_visible(self, locator, timeout=10):
        """Поиск и ожидание нескольких видимых элементов"""
        return WebDriverWait(self.driver, timeout, poll_frequency=1). \
            until(EC.visibility_of_all_elements_located(locator))
