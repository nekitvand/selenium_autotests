from base import Base, Locators


class MainPageLocators:
    TABS = (Locators.CSS_SELECTOR, ".tm-main-menu__section-content a")


class MainPage(Base):

    def select_all_tabs(self):
        """Сбор всех вкладок меню"""
        return self.FindAction.finds(MainPageLocators.TABS)

    def click_to_tabs_by_name(self, tab_name):
        tabs = self.select_all_tabs()
        for tab in tabs:
            if tab_name in self.ElementAction.get_text_content(tab):
                return self.ElementAction.click(tab)
