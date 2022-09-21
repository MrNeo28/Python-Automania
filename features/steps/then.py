from behave import then


@then("User gets page title")
def get_title(context):
    # title = context.browser.title
    title = context.selenium.get_title
    print(f"Page title {title}")
