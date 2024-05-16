# webdriver_utils.py

from selenium.webdriver import Firefox
from selenium.webdriver import Chrome
# from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from helpers.explicity_wait import ExplicitWaitType
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


class WebdriverHandler:

    def __init__(self):
        self.driver = Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(0.7)
        self.wait = ExplicitWaitType(self.driver)
