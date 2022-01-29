class ElementAction:

    def __init__(self, driver):
        self.driver = driver

    def get_attribute_by_element(self, element, name):
        """Производит поиск значения атрибута по имени"""
        return element.get_attribute(name)

    def scroll_to_element(self, element):
        """Скролл веб страницы до указанного элемента"""
        return element.location_once_scrolled_into_view

    @classmethod
    def click(cls, element):
        """Кликает на указанный элемент"""
        element.click()

    @classmethod
    def send(cls, web_element, text):
        """Вводит текст в указанный элемент(поле ввода)"""
        web_element.clear()
        web_element.send_keys(text)

    @classmethod
    def get_text(cls, element):
        """Получает текст из указанного элемента"""
        return element.text

    @classmethod
    def get_text_content(cls, element):
        """Получает текст из указанного элемента по атрибуту textContent"""
        return element.get_attribute('textContent')