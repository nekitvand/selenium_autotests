import allure
import pytest
from tests.main_page.data_main_page import NAME_TAB
from pages.main import MainPage


@allure.feature('Main page')
class TestMainPage:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        self.main_page = MainPage(browser)

    @allure.title('Проверка перехода по страницам быстрой навигации')
    @pytest.mark.parametrize("tab, must_url", NAME_TAB)
    def test_click_on_the_tab(self, tab, must_url):
        with allure.step('Проверка перехода на страницу'):
            self.main_page.click_to_page_by_name(tab)
