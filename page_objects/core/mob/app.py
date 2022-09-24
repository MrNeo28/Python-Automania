""" Mobile device related functions"""
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy as By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException


import os, time
import structlog

logger = structlog.get_logger(__name__)

class App:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def find_element_by_id(self, locator:str):
        wait = WebDriverWait(self.driver, 10)

        try:
            wait.until(EC.visibility_of_any_elements_located((By.ACCESSIBILITY_ID, locator)))
        except NoSuchElementException:
            logger.error(f"element failed attempt {locator} by ID")

    def find_element_by_xpath(self, locator:str):
        wait = WebDriverWait(self.driver, 10)

        try:
            wait.until(EC.visibility_of_any_elements_located((By.XPATH, locator)))
        except NoSuchElementException:
            logger.error(f"element failed attempt {locator} by Xpath")

    def find_element_by_class_name(self, locator:str):
        wait = WebDriverWait(self.driver, 10)

        try:
            wait.until(EC.visibility_of_any_elements_located((By.CLASS_NAME, locator)))
        except NoSuchElementException:
            logger.error(f"element failed attempt {locator} by Class name")

    