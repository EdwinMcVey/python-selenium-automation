from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from time import sleep

@given ('Open Amazon Home page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@given ('Open Help Customer page')
def open_help_customer_page(context):
    context.driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_custrec_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

@when ('Click on New Customer? Start Here')
def click_start_here(context):
    sleep(5)
    context.driver.find_element(By.XPATH, "//a[@href='https://www.amazon.com/-/es/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F-%2Fes%2F%3F_encoding%3DUTF8%26language%3Des%26ref_%3Dnav_custrec_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&']").click()

@then ('Verify Your Name Block is present')
def verify_your_name_block_present(context):
    context.driver.find_element(By.ID, 'ap_customer_name')
    expected_results = 'Your name'
    actual_results = context.driver.find_element(By.ID, 'ap_customer_name')

