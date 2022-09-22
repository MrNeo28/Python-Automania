from behave import given



@given("User maximize current window")
def max_window(context):
    context.selenium.maximize_window()

@given('User navigates to "{text}"')
def goto_url(context, text):
    context.selenium.navigate_url("https://www.google.com/")
