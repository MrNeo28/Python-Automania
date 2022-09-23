from multiprocessing import context
from behave import when
from selenium.webdriver.common.by import By


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
