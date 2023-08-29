# from selenium.webdriver.common.by import By
# from behave import given, when, then
# from time import sleep
#
# SEARCH_BTN = (By.CSS_SELECTOR, '#nav-search-submit-button')
# ALL_PRODUCTS = (By.CSS_SELECTOR, '[data-component-type="s-search-result"]')
#
#
# @when('Look for item')
# def search_product(context):
#     context_product = context.driver.find_element(By.ID, 'twotabsearchtextbox')
#     context_product.clear()
#     context_product.send_keys('dress')
#
#
# @when('Click on search button')
# def search_button(context):
#     context.driver.find_element(*SEARCH_BTN).click()
#
#
# @then('Verify every product has name and image')
# def product_has_name_and_image(context):
#     all_products = context.driver.find_elements(*ALL_PRODUCTS)
#     assert len(all_products) == 60
#     for product in all_products:
#         image = product.find_element(By.CLASS_NAME, 's-product-image-container')
#         title = product.find_element(By.CLASS_NAME, 's-title-instructions-style')
#         assert image is not None
#         assert title is not None
#


