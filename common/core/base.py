from selenium import webdriver

from core.web.elements import Finder
from core.web.browser import Browser


def get_browser(browser):
    if browser == "chrome":
        return Finder(driver)
