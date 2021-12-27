from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@then('Verify Create your Amazon Account button is present')
def verify_create_account_btn(context):
    context.driver.find_element(By.CLASS_NAME, 'a-button-text').text
    expected_results = 'Create your Account Account'
    actual_results = context.driver.find_element(By.CLASS_NAME, 'a-button-text')

