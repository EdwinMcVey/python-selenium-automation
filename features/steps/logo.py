from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@then ('Verify Amazon Logo is present')
def verify_logo_present(context):
    context.driver.find_element(By.XPATH, "//a[@class='a-link-nav-icon']")

