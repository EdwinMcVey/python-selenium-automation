from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

TOP_LINK = (By.CSS_SELECTOR, 'div._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq ul li')
HEADER = (By.CSS_SELECTOR, '#zg_banner_text')


@then('User can click through top links and verify correct page opens')
def click_thru_top(context):
    top_links = context.driver.find_elements(*TOP_LINK)
    print(top_links)

    for x in range(len(top_links)):
        link = context.driver.find_elements(*TOP_LINK)[x]
        link_text = link.text
        print(link_text)
        link.click()

        header_text = context.driver.find_element(*HEADER).text
        assert link_text in header_text, f'Expected {link_text} not in {header_text}'
