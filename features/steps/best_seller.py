from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Best seller page')
def best_seller(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

@then('Verify 5 tabs are visible')
def tabs_visible(context):
    list_items = context.driver.find_elements(By.CSS_SELECTOR, "#zg_header a")
    assert len(list_items) == 5
