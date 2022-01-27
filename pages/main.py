from base import Base

class MainPageLocators:
    pass




class MainPage(Base):

    def __init__(self, driver):
        pass


class Null(MainPage):

    def __init__(self, driver):
        super().__init__(driver)

    def xxx(self):
        self.FindAction.find()