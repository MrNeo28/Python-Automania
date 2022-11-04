from behave import when
from selenium.webdriver.common.by import By
from assertpy import assert_that


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
    context.selenium.find_element_by_xpath(context.parse_locator(locator)).send_keys(MovieName)


@when("User clicks on '{locator}'")
def click_button(context, locator):
    context.selenium.find_element_by_xpath(context.parse_locator(locator)).click()


@when("User clicks on search result '{locator}' of '{MovieName}'")
def click_search(context, locator: str, MovieName: str):
    context.selenium.find_element_by_xpath(context.parse_locator(locator) % MovieName).click()


@when("User is on '{MovieName}' screen")
def assert_screen(context, MovieName: str):
    title = context.selenium.get_title
    # assert context.selenium.get_title == MovieName, f"Current movie title {text} but excepted title {MovieName}"
    assert_that(title).contains_ignoring_case(MovieName)

@when("User gets '{origin}' is '{country}'")
def get_text(context, origin: str, country: str):
    text = context.selenium.find_element_by_xpath(context.parse_locator(origin)).text
    assert_that(country).is_equal_to_ignoring_case(text)


@when("User gets '{date}' on '{actual_date}'")
def get_text(context, date: str, actual_date: str):
    text = context.selenium.find_element_by_xpath(context.parse_locator(date)).text
    assert_that(date).contains(actual_date)

@when("User pause for '{wait:d}' s")
def wait(context, wait: int):
    # implicitly_wait is not recommended
    context.selenium.wait_until(wait)