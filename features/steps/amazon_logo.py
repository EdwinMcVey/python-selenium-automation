from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@given('New Customer page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/cus')

@when('Click on Search Help Library')
def click(context):
    context.driver.find_element(By.XPATH, "//input[@id='helpsearch']").click
@when(')
def input(context):
    context.driver.find_element(By.XPATH,

@then("Verify ‘Amazon logo is present")
def verify(context):
    actual_result = context.driver.find_element(XPATH, "//a[@class='a-link-nav-icon']/i").text.text
    expected_result = "Amazon logo"

    assert actual_result == expected_result, f'Error, actual {actual_result} did not match {expected_result}'
