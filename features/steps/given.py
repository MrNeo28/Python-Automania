from behave import given


@given('User navigates to "{text}"')
def goto_url(text):
    print(f"user go to {text}")
