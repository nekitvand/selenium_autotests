from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageAction:

    def __init__(self, driver):
        self.driver = driver

    def close_current_window(self):
        """Закрывает текущее окно"""
        return self.driver.close()

    def get_window_handles(self):
        """Возвращает хэндлы(индетификторы) для всех окон в текущей сессии"""
        return self.driver.window_handles

    def current_window_handle(self):
        """Выводит хэндл(индетификтор) текущего окона, с которым работает драйвер"""
        return self.driver.current_window_handle

    def back_to_previous_page(self):
        """Возвращает на предыдущую страницу"""
        return self.driver.back()

    def forward_in_page(self):
        """"Переходит вперед по страницам сохраненым в истории"""
        return self.driver.forward()

    def fullscreen_window(self):
        """Отправляет команду менеджеру окон об открытии на весь экран"""
        return self.driver.fullscreen_window()

    def set_window_position(self, x, y):
        """Задает позицию для окна(по умолчанию - текущее)"""
        return self.driver.set_window_position(x, y, )

    def set_window_rect(self, x, y, width, height):
        """"Задает координаты для текущего окна (x,y,ширина и высота)"""
        return self.driver.set_window_position(x, y, width, height)

    def set_window_size(self, width, height):
        """Задает координаты для текущего окна(Ширина и высота)"""
        return self.driver.set_window_size(width, height)

    def get_window_position(self, windowhandle='current'):
        """"Получает координаты X,Y окна (по умолчанию - текущее)"""
        return self.driver.get_window_position(windowhandle)

    def get_window_rect(self):
        """Получает координаты X,Y окна (по умолчанию - текущее), ширину и высоту"""
        return self.driver.get_window_rect()

    def get_window_size(self, windowhandle='current'):
        """Возвращает ширину и высоту окна (по умолчанию - текущее) """
        return self.driver.get_window_size(windowhandle)

    @property
    def switch_to(self):
        """ Обеспечивает переключение на необходимый элемент
        driver.switch_to.active_element
        alert = driver.switch_to.alert
        driver.switch_to.default_content()
        driver.switch_to.frame(1)
         driver.switch_to.frame(driver.find_elements_by_tag_name(“iframe”)[0])
         driver.switch_to.parent_frame()
         driver.switch_to.window(‘main’)"""
        return self.driver.switch_to

    def refresh_page(self):
        """"Перезагружает страницу с ожиданием"""
        self.driver.refresh()

    def go_to_base_url(self):
        """Переход на узказанный URL в conf.ini,либо принимается из cli"""
        return self.driver.get(self.driver.url)

    def go_to_page(self, page):
        """Переход на указнную страницу"""
        return self.driver.get(page)