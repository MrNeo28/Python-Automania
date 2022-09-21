from behave import given


@given('User navigates to "{text}"')
def goto_url(context, text):
    context.selenium_generics.navigate_url(text)
