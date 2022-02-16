from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from pages.header import Header


@given('Open Amazon page')
def open(context):
    context.app.main_page.open_page_main()


@when('Click Amazon Orders link')
def search_orders(context):
    context.app.header.search_orders()


@then('Verify Sign in page is opened')
def open_page(context):
    context.app.main_page.verify_page()

