from selenium.webdriver.common.by import By
from behave import given, when, then


COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
SELECTED_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')


@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}')


@then('Verify user can click through colors')
def verify_can_click_colors(context):
    expected_colors = ['Army Green', 'Black', 'Blue', 'Brown']

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for k in range(len(colors[:4])):
        colors[k].click()
        actual_colors = context.driver.find_element(*SELECTED_COLOR).text

        print(actual_colors)
    assert actual_colors == expected_colors[k], f'Expected {expected_colors[k]}, but got {actual_colors}'

