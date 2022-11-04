from behave import when
from selenium.webdriver.common.by import By
from features.locators.locators import get_locator


@when('User enters "{search_text}" text in search box')
def enter_text(context, search_text):
    context.selenium.find_element_by_xpath('//input[@class="gLFyf gsfi"]').send_keys(
        search_text
    )


@when("User clicks search button")
def click_search_btn(context):
    context.selenium.find_element_by_xpath(
        '//input[@aria-label="Google Search"]'
    ).click()


@when("User enters text '{MovieName}' on '{locator}'")
def enter_text(context, MovieName: str, locator: str):
    context.selenium.find_element_by_xpath(get_locator(locator)).send_keys(MovieName)


@when("User clicks on '{locator}'")
def click_button(context, locator):
    context.selenium.find_element_by_xpath(get_locator(locator))


@when("User clicks on search results '{locator}'")
def click_search(context, locator: str):
    context.selenium.find_element_by_xpath(get_locator(locator))


@when("User is on '{MovieName}' screen")
def assert_screen(context, MovieName: str):
    assert context.selenium.get_title == MovieName


@when("User gets {locator}")
def get_text(context, locator: str):
    text = context.selenium.find_element_by_xpath(get_locator(locator)).text
    print(text)
