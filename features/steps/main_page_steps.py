from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



SEARCH_FIELD = (By.ID, "twotabsearchtextbox")
SEARCH_BTN = (By.ID, "nav-search-submit-button")
ORDER_BTN = (By.ID, 'nav-orders')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescItems')
SIGNIN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-signin-button')
SEARCH_RESULT = (By.CSS_SELECTOR, '.a-color-state a-text-bold')

@given('Open Amazon page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com')
    context.app.main_page.open_main()

@when('Search for {product}')
def search_on_amazon(context, product):
    # context.driver.find_element(*SEARCH_FIELD).send_key(product)
    # context.driver.find_element(*SEARCH_BTN).click()
    context.app.header.search_product(product)

@when('Click Orders')
def click_orders(context):
    context.driver.find_elemenr(*ORDER_BTN).click()

@then('Verify search result is {expected_result}')
def verify_search_result(context, expected_result):
    context.app.search_result.verify_search_result(expected_result)
