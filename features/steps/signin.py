from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@when('Click Amazon Orders link')
def click_order(context):
    context.app.header.click_order()


@then('Verify Sign In page is opened')
def verify_signin_page(context):
    context.app.signin_page.verify_signin_page('Sign in')
    self.verify_partial_url('ap/signin')

@when('Wait for 3 sec')
def wait_sec(context):
    sleep(3)

@then('Verify Sign In is clickable')
def verify_sigin_btn_clickable(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(SIGNIN)
    )