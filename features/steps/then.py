from behave import then


@then("User gets page title")
def get_title(context):
    # title = context.browser.title
    title = context.selenium.get_title
    print(f"Page title {title}")


@then("User clicks on first link")
def click_link(context):
    context.selenium.find_element_by_xpath(
        "(//a[contains(@href, 'github')])[1]"
    ).click()
