from pages.main import MainPage


def test_click_on_the_tab(browser):
    main_page = MainPage(browser)
    main_page.click_to_tabs_by_name("Разработка")
