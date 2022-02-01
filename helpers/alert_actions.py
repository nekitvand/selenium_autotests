from selenium.webdriver.common.alert import Alert


class AlertAction:

    def __init__(self, driver):
        self.driver = driver
        self.alert_action = Alert(self.driver)

    def alert_accept(self):
        """Принимает аллерт"""
        return self.alert_action.accept()

    def alert_dismiss(self):
        """Отклоняет аллерт"""
        return self.alert_action.dismiss()

    def alert_send_keys(self, key):
        """Вводит в поле вода"""
        return self.alert_action.send_keys(key)

    def alert_get_text(self):
        """Получает текст с аллерта"""
        return self.alert_action.text
