from pages.base_page import Page
from selenium.webdriver.common.by import By

class SignInPage(Page):
    SIGNIN = (By.CSS_SELECTOR, 'h1.a-spacing-small')
    EMAIL_FIELD = (By.ID, 'ap_email')



    def signin_page(self, expected_text):
        actual_text = self.find.element(*self.SIGNIN).text
        assert actual_text == expected_text, f'Error, expected {expected_text} did not match actual {actual_text} '
