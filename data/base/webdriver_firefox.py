from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import Firefox
from helpers.explicity_wait import ExplicitWaitType


class WebdriverHandler:
    def __init__(self):
        self.driver = Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(0.7)
        self.wait = ExplicitWaitType(self.driver)