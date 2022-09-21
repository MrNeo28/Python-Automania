"""
contains browser specific objects
"""
from selenium.webdriver.remote.webdriver import WebDriver


class Browser:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def navigate_url(self, url: str):
        self.driver.get(url)

    def maximize_window(self):
        self.driver.maximize_window()
