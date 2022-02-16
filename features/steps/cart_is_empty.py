from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from pages.main_page import MainPage
from pages.header import Header


@when('Click on Cart Icon')
def click_cart(self):
    self.driver.app.header.click_cart(*self.CART).click()

@then('Verify "Your Amazon Cart is empty" text present')
def verify_text(self, expected_text):
    expected_text = f'Your Amazon Cart is Empty'
    actual_text = self.driver.find_element(*self.CART_EMPTY).text
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
