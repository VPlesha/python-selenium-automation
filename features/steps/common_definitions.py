from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open amazon home page')
def open_amazon_home_page(context):
    context.driver.get('https://www.amazon.com/')
