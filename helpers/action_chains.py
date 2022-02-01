from selenium.webdriver import ActionChains


class ActionChain:

    def __init__(self, driver):
        self.driver = driver

    def __call__(self, *args, **kwargs):
        return ActionChains(self.driver)