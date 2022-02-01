class ExecuteScript:

    def __init__(self, driver):
        self.driver = driver

    def execute_js_script(self, text):
        """Выполняет кастомый js скприт"""
        return self.driver.execute_script(text)