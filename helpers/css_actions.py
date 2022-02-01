class CssAction:

    def get_any_ccs_property(self, element, ccs_property):
        """Позволяет получить любое ccs свойство по названию у элемента"""
        return element.value_of_css_property(ccs_property)

    def get_background_color(self, element):
        """Получить свойство background-color у элемента"""
        return element.value_of_css_property("background-color")