from behave import given


@given("User maximize current window")
def max_window(context):
    context.selenium.maximize_window()


@given('User navigates to "{text}"')
def goto_url(context, text):
    context.selenium.navigate_url("https://www.google.com/")

@given("User is on url '(?P<url>.*)'")
def visit_url(context, url: str):
    context.selenium.navigate_url(url)


