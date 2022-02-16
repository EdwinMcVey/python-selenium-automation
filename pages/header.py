from pages.base_page import Page
from selenium.webdriver.common.by import By

class Header(Page):
    CART = (By.CSS_SELECTOR, '#nav-cart-count')
    CART_EMPTY = (By.XPATH, "//h1[@class = 'a-spacing-mini a-spacing-top-base']")
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    SEARCH_ORDERS = (By.ID, 'nav-orders')


    def search_input(self, text):
        self.input_text(text, *self.SEARCH_INPUT)


    def search_orders(self):
        self.click(*self.SEARCH_ORDERS)

    def click_cart(self):
        self.click(*self.CART)


    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def cart_empty(self):
        self.cart_empty(*self.CART_EMPTY)