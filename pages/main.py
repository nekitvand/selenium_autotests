import allure

from core.base import Base, Locators


class MainPageLocators:
    TABS = (Locators.CSS_SELECTOR, ".tm-main-menu__section-content a")


class MainPage(Base):

    @allure.step('Собирает элементы всех страниц')
    def select_all_pages(self):
        """Сбор всех вкладок меню"""
        return self.FindAction.finds(MainPageLocators.TABS)

    @allure.step('Кликает на название страниц для перехода')
    def click_to_page_by_name(self, tab_name):
        tabs = self.select_all_pages()
        for tab in tabs:
            if tab_name in self.ElementAction.get_text_content(tab):
                return self.ElementAction.click(tab)

    @allure.step('Получает url страницы')
    def get_url_in_tab(self, must_url):
        url = self.UrlAction.get_current_url()
        if must_url in url:
            return True
        else:
            return Exception("Неверный url")

