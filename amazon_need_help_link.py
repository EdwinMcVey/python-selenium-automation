from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/chromedriver.exe")

driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

driver.find_element(By.CLASS_NAME, 'a-expander-prompt').click()

actual_text = driver.find_element(By.CLASS_NAME, 'a-expander-prompt').text
expected_text = 'Need help?'

assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

driver.quit()
