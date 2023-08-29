from pages.main_page import MainPage
from pages.header import Header
from pages.search_result import SearchResult

class Application:

    def __init__(self, driver):

        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_result = SearchResult(driver)

# app = Application()
# app.main_page.open_main()
# app.header.search_product()

