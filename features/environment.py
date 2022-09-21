from common.core.web.selenium_generics import Selenium

from behave import fixture, use_fixture
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@fixture
def selenium_generics(context):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return Selenium(driver)


def before_all(context):
    use_fixture(selenium_generics, context)