from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

counter = 0
@given('Open amazon product page with multiple colors')
def open_amazon_product_page(context):
    context.driver.get('https://www.amazon.com/gp/product/B07BJKRR25/')


@when('Click available color')
def click_each_color(context):
    global counter
    all_colors = context.driver.find_elements(By.CLASS_NAME, 'swatchAvailable')
    counter = len(all_colors)
    for knopka in all_colors:
        knopka.click()
        element_text = context.driver.find_element(By.ID, knopka.get_attribute('id'))
        assert element_text.get_attribute('class') == 'swatchSelect'
        counter = counter - 1

@then('All colors were selected one by one')
def verify_signin_opens(context):
    global counter
    assert counter == 0
    print("Test passed!")