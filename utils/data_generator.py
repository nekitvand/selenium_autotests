from mimesis import Generic
from mimesis.locales import Locale


class DataRU:

    def __init__(self):
        self.generic = Generic(locale=Locale.RU)

    def random_text(self):
        return self.generic.text.word()


