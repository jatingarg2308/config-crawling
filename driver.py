from selenium import webdriver

def get_driver():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--headless")
    driver = webdriver.Remote(
        command_executor="http://localhost:2020/wd/hub",
        options=firefox_options
    )
    driver.get("https://www.tartanhq.com/")
    return driver