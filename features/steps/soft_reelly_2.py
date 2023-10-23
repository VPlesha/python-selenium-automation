
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SETTING = (By.XPATH, "//a[contains(@href, '/settings')]")
SETTING_PAGE = (By.CSS_SELECTOR, ".body-setting")

driver = webdriver.Chrome()


@given("Open the main page")
def open_main_page(context):
    context.driver.get('https://soft.reelly.io/')
    sleep(1)


@when("Log in to the page")
def login_to_page(context):
    sleep(2)
    context.driver.find_element(By.ID, "email-2").send_keys("viktoriaplesha@gmail.com")
    sleep(2)
    context.driver.find_element(By.ID, "field").send_keys("Gfhjkm24!")
    sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, "a.login-button.w-button").click()
    sleep(2)


@when("Click on settings option")
def settings(context):
    sleep(2)
    context.driver.find_element(By.XPATH, "//a[contains(@href, '/settings')]").click()



@when("Verify the right page opens")
def setting_page(context):
    context.driver.find_element(By.CSS_SELECTOR, ".body-setting")


@when("Click on each settings option and go back (except on log out)")
def click_on_each_option(context):
    # list_options = context.driver.find_elements(By.CSS_SELECTOR, ".page-setting-block.w-inline-block")
    # for i in range(len(list_options)-1):
        # sleep(2)
        # list_options[i].click()
        # # sleep(2)
        #
    sleep(2)
    context.driver.find_element(By.XPATH, "//a[contains(@href, '/add-a-project')]").click()
    sleep(2)
    context.driver.find_element(By.XPATH, "//a[contains(@href, '/settings')]").click()
    sleep(2)
    context.driver.find_element(By.XPATH, "//a[contains(@href, '/profile-edit')]").click()
    sleep(2)
    context.driver.find_element(By.XPATH, "//a[contains(@href, '/settings')]").click()
    sleep(2)
    context.driver.find_element(By.XPATH, "//a[@href='https://wa.me/message/ULET72INKB57H1']").click()
    # context.driver.find_element(By.XPATH, "//a[contains(@href, '/settings')]").click()
    driver.close()
    context.driver.find_element(By.XPATH, "//a[contains(@href, 'https://t.me/reellydxb')]").click()
    context.driver.find_element(By.XPATH, "//a[contains(@href, '/settings')]").click()
    context.driver.find_element(By.XPATH, "//a[contains(@href, '/community')]").click()
    context.driver.find_element(By.XPATH, "//a[contains(@href, '/settings')]").click()
    context.driver.find_element(By.XPATH, "//a[contains(@href, '/user-guide')]").click()
    context.driver.find_element(By.XPATH, "//a[contains(@href, '/settings')]").click()
    context.driver.find_element(By.XPATH, "//a[contains(@href, '/verification/step-0')]").click()
    context.driver.find_element(By.XPATH, "//a[contains(@href, '/settings')]").click()
    context.driver.find_element(By.XPATH, "//a[contains(@href, '/set-new-password')]").click()
    context.driver.find_element(By.XPATH, "//a[contains(@href, '/settings')]").click().context.driver.find_element(By.XPATH, "//a[contains(@href, '/add-a-project')]").click()
    context.driver.find_element(By.XPATH, "//a[contains(@href, '/subscription')]").click().context.driver.find_element(By.XPATH, "//a[contains(@href, '/add-a-project')]").click()
    context.driver.find_element(By.XPATH, "//a[contains(@href, '/settings')]").click()

@then("Verify there are 11 options for the settings")
def verify_options(context):
    list_options = context.driver.find_element(By.CSS_SELECTOR, ".page-setting-block.w-inline-block")
    assert len(list_options) == 11
    print("Test passed: There are 11 settings options")

