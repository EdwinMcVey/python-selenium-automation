from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@then('Verify Sign-In is present')
def verify_sign_in(context):
    actual_results = context.driver.find_element(By.CSS_SELECTOR, "a.a-link-emphasis").text
    expected_results = 'Sign-In'
    assert actual_results == expected_results, f"got {actual_results}"