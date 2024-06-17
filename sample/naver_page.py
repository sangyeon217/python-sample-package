class NaverPage:

    def __init__(self, driver):
        self.driver = driver
        self.page_url = "https://www.naver.com"

    def goto(self):
        self.driver.get(self.page_url)
