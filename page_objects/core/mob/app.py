""" Mobile device related functions"""
from selenium.webdriver.remote.webdriver import WebDriver

class App:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_elements(self):
        pass
