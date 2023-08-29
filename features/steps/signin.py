from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click Amazon Orders link')
def click_order(context):
    context.app.header.click_order()


@then('Verify Sign In page is opened')
def verify_signin_page(context, expected_text):
    context.app.signin_page.verify_signin_page(expected_text)


