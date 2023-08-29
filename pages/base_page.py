class Page:

    def __init__(self,driver):
        self.driver = driver

    def clcik(self, *locator):
        self.driver.find_element(*locator).click()
    def find_element(self, *locator):
        return self.driver.find_element(*locator)


    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.send.keys(text)
