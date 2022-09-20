import allure, os, time
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
import sys
import structlog

logger = structlog.get_logger(__name__)

class App:

    def __init__(self, driver):
        self.driver = driver