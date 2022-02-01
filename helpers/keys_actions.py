from selenium.webdriver.common.keys import Keys


class KeysAction:

    def __call__(self, *args, **kwargs):
        return Keys()