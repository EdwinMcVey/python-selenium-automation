from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PRODUCT_PRICE = (By.XPATH, "//span[@class='a-price']")
CART = (By.CSS_SELECTOR, '#nav-cart-count')
ADD_TO_CART_BTN = By.ID, 'add-to-cart-button'
CART_BTN = (By.ID, 'attach-sidesheet-view-cart-button')

@given ('Open Amazon Page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com')


@when('Search for {query}')
def search_amazon(context, query):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(query)


@when('Click search icon')
def click_search_icon(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@when('Click on first item')
def click_first_item(context):
    context.driver.find_element(*PRODUCT_PRICE).click()


@when('Click on Add to cart button')
def click_add_to_cart(context):
    e = context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BTN), message='button not clickable')
    e.click()
    white_button = context.driver.wait.until(EC.element_to_be_clickable(CART_BTN), message='button not clickable')
    white_button.click()


@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    actual_count = context.driver.find_element(*CART).text
    assert actual_count == expected_count, f'Error actual {actual_count} did not match expected {expected_count}.'

