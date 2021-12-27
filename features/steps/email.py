from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

@then('Verify Email is present')
def verify_your_name(context):
    context.driver.find_element(By.ID, 'ap_email')
    expected_results = 'Email'
    actual_results = context.driver.find_element(By.ID, 'ap_email')

