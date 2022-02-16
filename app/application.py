from pages.main_page import MainPage
from pages.header import Header

class Application:

    def __init__(self, driver) -> None:
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)