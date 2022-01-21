from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC



PN_LINK = (By.XPATH, "//a[@href = ('https://www.amazon.com/privacy')]")

@given('Open Amazon T&C page')
def open_amazon_tc_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_window(context):
    context.original_window = context.driver.current_window_handle
    print('Original window:', context.original_window)


@when('Click on Amazon Privacy Notice link')
def click_pn_link(context):
    context.driver.find_element(*PN_LINK).click()


@when('Switch to the newly opened page')
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles
    context.driver.switch_to.window(windows[1])


@then('Verify Amazon Privacy Notice page is opened')
def amazon_pn_opened(context):
    assert 'https://www.amazon.com/' in context.driver.current_url, f'Privacy Notice page did not open'


@then('User can close new window')
def close_pn_window(context):
    context.driver.close()

@then('Switch back to original')
def return_to_tc_page(context):
    context.driver.switch_to.window(context.original_window)


