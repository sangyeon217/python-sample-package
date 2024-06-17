class GooglePage:

    def __init__(self, driver):
        self.driver = driver
        self.page_url = "https://www.google.com"

    def goto(self):
        self.driver.get(self.page_url)
