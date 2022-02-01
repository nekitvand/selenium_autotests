class CookiesAction:

    def __init__(self, driver):
        self.driver = driver

    def add_cookie(self, cookie_dict):
        """Добавить cookie с текущей сессии """
        self.driver.add_cookie(cookie_dict)

    def get_cookies(self):
        """Получить все cookies из текущего сеанса"""
        return self.driver.get_cookies()

    def get_cookie(self, name):
        """Получить cookie по имени"""
        return self.driver.get_cookie(name)

    def delete_single_cookie(self, cookie_name):
        """Удаляет одиночно cookie по ее названию"""
        return self.driver.delete_cookie(cookie_name)

    def delete_all_cookies(self):
        """Удалить cookies с текущей сессии"""
        return self.driver.delete_all_cookies()

    def application_cache(self):
        """Возвращает ApplicationCache Object"""
        return self.driver.application_cache