import time

from selenium import webdriver
import send_allure



def test_x():
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "97.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }

    driver = webdriver.Remote(
        command_executor="http://selenoid:4444/wd/hub",
        desired_capabilities=capabilities)

    driver.get("http://ya.ru")
    driver.get("https://stackoverflow.com/")
    driver.quit()

