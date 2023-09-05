from pages.base_page import Page
from selenium.webdriver.common.by import By

class SearchResult(Page):
    SEARCH_RESULT = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')

    def verify_search_result(self, expected_text):
        # actual_text = self.find_element(*self.SEARCH_RESULT).text
        # assert actual_text == expected_text, f'Error, expected {expected_text} did not match actual {actual_text}'
        self.verify_text(expected_text, *self.SEARCH_RESULT)

