from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@then ('Verify Create Account Page Opened')
def verify_create_acct_page_opened(context):
##   context.driver.find_element(By.CLASS, 'a-spacing-small')
    expected_header = 'Create account'
    actual_header = context.driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small").text
    print(actual_header)
    assert actual_header == expected_header






