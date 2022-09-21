from behave import then


@then("User gets page title")
def get_title(context):
    print("Title: Google")
