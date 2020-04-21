"""
Selenium steps to configure behave test scenarios
"""
import time

@when('visit url "{url}"')
def step(context, url):
    context.browser.maximize_window()
    context.browser.get(url)


@when('check if title is "{title}"')
def step(context, title):
    assert context.browser.title == title


@when('field with name "First Item" is present check the box')
def step(context):
    context.browser.find_element_by_name("li1").click()


@when('field with name "Second Item" is present check the box')
def step(context):
    context.browser.find_element_by_name("li3").click()


@when('select the textbox add "{text}" in the box')
def step(context, text):
    context.browser.find_element_by_id("sampletodotext").click()
    context.browser.find_element_by_id("sampletodotext").clear()
    context.browser.find_element_by_id("sampletodotext").send_keys(text)


@then('click the "{button}"')
def step(context, button):
    context.browser.find_element_by_id(button).click()