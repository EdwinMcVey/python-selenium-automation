from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@then('Verify Conditions of Use is present')
def verify_conditions_of_use(context):
    context.driver.find_element(By.XPATH,  "//a[@href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")
    expected_results = 'Conditions of Use'
    actual_results = context.driver.find_element(By.XPATH, "//a[@href= '/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")
    expected_results = 'Conditions of Use'

