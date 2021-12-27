from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@then('Verify Privacy Notice is present')
def verify_privacy_notice(context):
    expected_results = 'Privacy Notice'
    actual_results = context.driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496']").text
    assert actual_results == expected_results, f"got {actual_results}"