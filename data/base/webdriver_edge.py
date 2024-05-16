from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver import Edge
from helpers.explicity_wait import ExplicitWaitType

class WebdriverHandler:
    def __init__(self):
        self.driver = Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(0.7)
        self.wait = ExplicitWaitType(self.driver)