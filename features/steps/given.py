from behave import given


@given('User navigates to "{text}"')
def goto_url(context, text):
    print(f"user go to {text}")
