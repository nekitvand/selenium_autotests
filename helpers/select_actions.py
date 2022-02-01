from selenium.webdriver.support.select import Select


class SelectAction:

    def __init__(self, driver):
        self.driver = driver

    def get_select(self, element):
        return Select(element)

    def all_selected_options(self, element):
        """Возвращает список параметров для выбранного тега(элемента)"""
        return self.get_select(element).all_selected_options

    def first_selected_option(self, element):
        """Возвращает первый параметр для выбранного тега(элемента)"""
        return self.get_select(element).first_selected_option

    def select_by_index(self, element, index):
        """Возвращает параметр по индексу, для выбранного тега(элемента)"""
        return self.get_select(element).select_by_index(index)

    def select_by_value(self, element, value):
        """Возвращает параметр по значению, для выбранного тега(элемента)"""
        return self.get_select(element).select_by_value(value)

    def select_by_visible_text(self, element, text):
        """Возвращает параметр по тексту, для выбранного тега(элемента)"""
        return self.get_select(element).select_by_visible_text(text)

    def select_list_options(self, element):
        """Возвращает список названий опций селектора."""
        return [option.text for option in self.get_select(element).options]
