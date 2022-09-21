from behave import given


@given('User navigates to "{text}"')
def goto_url(context, text):
    # context.browser.get("https://www.google.com/")
    context.selenium.navigate_url("https://www.google.com/")
