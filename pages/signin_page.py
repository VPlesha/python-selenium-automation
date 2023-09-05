from pages.base_page import Page
from selenium.webdriver.common.by import By

class SignInPage(Page):
    SIGNIN = (By.CSS_SELECTOR, 'h1.a-spacing-small')
    EMAIL_FIELD = (By.ID, 'ap_email')



    def verify_signin_page(self, expected_text):
        # actual_text = self.driver.find_element(*self.SIGNIN).text
        self.verify_text('Sign in', *self.SIGNIN)

        # assert actual_text == expected_text, f'Error, expected {expected_text} did not match actual {actual_text} '
