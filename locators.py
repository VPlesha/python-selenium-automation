from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')


# By ID
driver.find_element(By. ID, 'twotabsearchtextbox')
driver.find_element(By. ID, 'nav-search-submit-button')

#By XPATH
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon']")

#By XPATH with quotes, exception
# driver.find_element(By.XPATH, '//img(@alt=\"Shopbop Mother's Day gifts\"])")

#By XPATH, multiple attributes
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon' and @aria-label='Search Amazon']")

#By XPATH, text
driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
#By XPATH, text and attr
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")

#By XPATH, contains
driver.find_element(By.XPATH, "//a[contains(@href, 'nav_cs_bestseller')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Best Sell')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Best Sell') and @class='nav-a  ']")

#By XPATH, parent child
driver.find_element(By.XPATH, "//div[@id='nav-xshop-container']//a[text()='Best Sellers']")