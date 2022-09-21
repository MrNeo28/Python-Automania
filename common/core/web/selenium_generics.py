"""contains common selenium functions"""

from selenium.webdriver.remote.webdriver import WebDriver

from common.core.web.browser import Browser
from common.core.web.elements import Finder
from common.core.mob.app import App

class Selenium(Browser, Finder, App):
    def __init__(self, driver: WebDriver):

        self._selenium = driver

        super().__init__(self._selenium)

    def components(self):
        pass
