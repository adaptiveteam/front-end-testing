from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


def sign_in(driver, workspace, username, password):
    Wait(driver=driver, timeout=10, poll_frequency=2).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="domain"]'))).send_keys(workspace)
    Wait(driver=driver, timeout=10, poll_frequency=2).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'button[id="submit_team_domain"]'))).click()
    Wait(driver=driver, timeout=10, poll_frequency=2).until(ec.presence_of_element_located((By.ID, 'email')))
    Wait(driver=driver, timeout=10, poll_frequency=2).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="email"]'))).send_keys(username)
    Wait(driver=driver, timeout=10, poll_frequency=2).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="password"]'))).send_keys(password)
    Wait(driver=driver, timeout=10, poll_frequency=2).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'button[id="signin_btn"]'))).click()


def select_adaptive(driver):
    Wait(driver=driver, timeout=10, poll_frequency=2).until(ec.element_to_be_clickable((By.XPATH, "//span[@class='p-channel_sidebar__name'] // span[contains(text(), 'adaptive')]"))).click()
    # Wait for menu creation
    driver.implicitly_wait(5)
    Wait(driver=driver, timeout=10, poll_frequency=2).until(ec.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'I am good for now, thank you!')]"))).click()
    Wait(driver=driver, timeout=10, poll_frequency=2).until(ec.element_to_be_clickable((By.XPATH, "//button[@class='c-button c-button--danger c-button--medium c-dialog__go null--danger null--medium']"))).click()
