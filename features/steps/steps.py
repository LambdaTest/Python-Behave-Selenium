"""
Selenium steps to configure behave test scenarios
"""
import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(context, by, value, timeout=10):
    return WebDriverWait(context.browser, timeout).until(
        EC.presence_of_element_located((by, value))
    )

@when('visit url "{url}"')
def step(context, url):
    context.browser.get(url)

@when('check if title is "{title}"')
def step(context, title):
    assert context.browser.title == title

@when('field with name "First Item" is present check the box')
def step(context):
    element = wait_for_element(context, By.NAME, "li1")
    element.click()

@when('field with name "Second Item" is present check the box')
def step(context):
    element = wait_for_element(context, By.NAME, "li3")
    element.click()

@when('select the textbox add "{text}" in the box')
def step(context, text):
    textbox = wait_for_element(context, By.ID, "sampletodotext")
    textbox.click()
    textbox.clear()
    textbox.send_keys(text)

@then('click the "{button}"')
def step(context, button):
    element = wait_for_element(context, By.ID, button)
    element.click()