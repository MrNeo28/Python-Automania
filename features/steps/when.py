from behave import when


@when('User enters "{search_text}" text in search box')
def enter_text(search_text):
    print(f"User enters: {search_text}")