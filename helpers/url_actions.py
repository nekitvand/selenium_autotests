from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class UrlAction:

    def __init__(self, driver):
        self.driver = driver

    def url_changes(self, url, time=2):
        """Метод для проверки текущего URL.
        Принимает :URL: для проверки
        Возвращает True, если url-адрес отличается, в противном случае false.
        :return: Возвращает обьект Webdriver"""
        return WebDriverWait(self.driver, time, poll_frequency=1). \
            until(EC.url_changes(url))

    def url_contains(self, url, time=2):
        """Метод для проверки текущего URL. Проверяет частичное совпадение.
        Принимает :URL: для проверки
        Возвращает True, если url-адрес частично совпадает, False в противном случае.
        :return: Возвращает обьект Webdriver"""
        return WebDriverWait(self.driver, time, poll_frequency=1). \
            until(EC.url_contains(url))

    def url_to_be(self, url, time=2):
        """Метод для проверки текущего URL. Проверяет точное совпадение.
        Принимает :URL: для проверки
        Возвращает True, если точно url-адрес совпадает, False в противном случае.
        :return: Возвращает обьект Webdriver"""
        return WebDriverWait(self.driver, time, poll_frequency=1). \
            until(EC.url_to_be(url))

    def get_current_url(self):
        """"Получает текущий URL страницы"""
        return self.driver.current_url
