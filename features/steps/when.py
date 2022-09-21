from behave import when
from selenium.webdriver.common.by import By


@when('User enters "{search_text}" text in search box')
def enter_text(context, search_text):
    print(f"User enters: {search_text}")
    el = context.selenium.find_element_by_xpath('//input[@class="gLFyf gsfi"]')
