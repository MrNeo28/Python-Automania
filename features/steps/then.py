from behave import then


@then('User gets page title')
def get_title():
    print("Title: Google")