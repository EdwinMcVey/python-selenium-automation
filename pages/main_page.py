from pages.base_page import Page


class MainPage(Page):

        def open_page_main(self):
            self.open_page()

        def verify_page(self):
            self.verify_url_contains_query('ap/signin')