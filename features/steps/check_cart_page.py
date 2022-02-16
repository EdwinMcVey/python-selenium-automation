from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from time import sleep


#@when('Click on Cart Icon')
#def click_cart_icon(context):
#    context.driver.find_element(By.ID, "nav-cart-count").click()
##   sleep(5)


#@then('Verify Your Amazon Cart is empty')
#def verify_amazon_cart_page(context):
#    actual_result = context.driver.find_element(By.CSS_SELECTOR, "div.a-row.sc-your-amazon-cart-is-empty h2").text
#    expected_result = "Your Amazon Cart is empty"
#    assert actual_result == expected_result, f'Error, actual {actual_result} did not match {expected_result}'
