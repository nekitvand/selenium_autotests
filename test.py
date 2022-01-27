from selenium import webdriver



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
        command_executor="http://localhost:4444/wd/hub",
        desired_capabilities=capabilities)

    driver.get("www.ya.ru")
    driver.quit()