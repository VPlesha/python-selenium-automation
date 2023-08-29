from pages.main_page import MainPage
from pages.header import Header
from pages.search_result import SearchResult
from pages.signin_page import SignInPage

class Application:

    def __init__(self, driver):

        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_result = SearchResult(driver)
        self.signin_page = SignInPage(driver)

# app = Application()
# app.main_page.open_main()
# app.header.search_product()

