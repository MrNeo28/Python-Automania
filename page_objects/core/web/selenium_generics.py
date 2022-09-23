"""contains common selenium functions"""

from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.core.web.browser import Browser
from page_objects.core.web.elements import Finder
from page_objects.core.mob.app import App


class Selenium(Browser, Finder, App):
    def __init__(self, driver: WebDriver):

        self._selenium = driver

        super().__init__(self._selenium)

    def components(self):
        pass
