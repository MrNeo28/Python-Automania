"""
Contains find web elements objects
"""

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException

from typing import List

import structlog

logger = structlog.get_logger(__name__)


class Finder:
    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

        super().__init__(self.driver)

    def find_element_by_xpath(self, locator) -> WebElement:

        wait = WebDriverWait(self.driver, 10)

        try:
            return wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        except NoSuchElementException:
            logger.error("Unable to locate element")

    def find_element_by_id(self, locator) -> WebElement:
        
        wait = WebDriverWait(self.driver, 10)
        try:
            return wait.until(EC.visibility_of_element_located((By.ID, locator)))
        except NoSuchElementException:
            logger.error("Unable to locate element")

    def find_element_by_name(self, locator: str) -> WebElement:
        try:
            return self.wait.until(EC.visibility_of_element_located((By.NAME, locator)))
        except NoSuchElementException:
            logger.error("Unable to locate element")

    def find_element_by_css(self, locator: str) -> WebElement:
        try:
            return self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, locator))
            )
        except NoSuchElementException:
            logger.error("Unable to locate element")

    def find_element_by_class(self, locator: str) -> WebElement:
        try:
            return self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, locator))
            )
        except NoSuchElementException:
            logger.error("Unable to locate element")

    def find_element_by_tag_name(self, locator: str) -> WebElement:
        try:
            return self.wait.until(
                EC.visibility_of_element_located((By.TAG_NAME, locator))
            )
        except NoSuchElementException:
            logger.error("Unable to locate element")

    def find_element_by_link_text(self, locator: str) -> WebElement:
        wait = WebDriverWait(self.driver, 10)
        try:
            return wait.until(EC.visibility_of_element_located((By.LINK_TEXT, locator)))
        except NoSuchElementException:
            logger.error("Unable to locate element")
