from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@then('Verify Re-enter Password Block is present')
def verify_re_enter_password(context):
    context.driver.find_element(By.ID, 'ap_password_check')
    expected_results = 'Email'
    actual_results = context.driver.find_element(By.ID, 'ap_password_check')

