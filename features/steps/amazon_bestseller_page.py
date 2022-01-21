from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

BEST_SELLERS_LINK = (By.XPATH, "//a[contains(@href, 'ref=zg_bs_tab')]")
@given('Open Amazon Best Sellers page')
def open_bestsellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=_nav_cs_bestsellers')


@then('Verify there are 5 links')
def verify_best_seller_links(context):
    best_seller_links = context.driver.find_elements(*BEST_SELLERS_LINK)
    assert len(best_seller_links) == 5, f'Expected 5 links, but found {len(best_seller_links)}'

