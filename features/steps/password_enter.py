from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@then('Verify Password  Block is present')
def verify_your_name(context):
    context.driver.find_element(By.ID, 'ap_password')
    expected_results = 'Email'
    actual_results = context.driver.find_element(By.ID, 'ap_password')

