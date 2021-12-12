from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


@given('Open Amazon Help page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Click on Search Help Library')
def click(context):
    context.driver.find_element(By.XPATH, "//input[@id='helpsearch']").click()





