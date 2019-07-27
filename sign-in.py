# Selenium 3.14+ doesn't enable certificate checking
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import urllib3
import certifi

# This is the only code you need to edit in this script.
# Enter in your Sauce Labs Credentials in order to run this test
sauce_username = "ctcreel"
sauce_access_key = "96e693b5-b59c-4cfd-8698-27c2b49f52a7"
# This variable contains the service address for the Sauce Labs VM hub
remote_url = "https://ondemand.saucelabs.com:443/wd/hub"
# The desired_capabilities parameter includes metadata specific to sauce labs
# including: username, accessKey, browserName, platform etc.
# parameter tells us which browsers and OS to spin up.

desired_cap = {
    'platform': 'Mac OS X 10.13',
    'browserName': 'chrome',
    'version': '75',
    'build': 'Onboarding Sample App - Python',
    'name': 'log in and say hi',
    'username': sauce_username,
    'accessKey': sauce_access_key,
    # This setting is for using Sauce Connect Proxy tunnel
    # Typically you use this setting if you need to run your tests from behind a secure network firewall
}

def signIn(driver):
    workspaceNameInput = driver.find_element_by_css_selector('input[id="domain"]')
    workspaceNameInput.send_keys(os.environ['WORKSPACE'])
    continueButton = driver.find_element_by_css_selector('button[id="submit_team_domain"]')
    continueButton.click()
    wait(driver, 10).until(EC.presence_of_element_located((By.ID, 'email')))
    usernameInput = driver.find_element_by_css_selector('input[id="email"]')
    usernameInput.send_keys(os.environ['USER_EMAIL'])
    passwordInput = driver.find_element_by_css_selector('input[id="password"]')
    passwordInput.send_keys(os.environ['USER_PASSWORD'])
    signInButton = driver.find_element_by_css_selector('button[id="signin_btn"]')
    signInButton.click()

def selectAdaptive(driver):
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='p-channel_sidebar__name'] // span[contains(text(), 'adaptive')]"))).click()
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'I am good for now, thank you!')]"))).click()
    wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='c-button c-button--danger c-button--medium c-dialog__go null--danger null--medium']"))).click()

http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
driver = webdriver.Remote(command_executor=remote_url, desired_capabilities=desired_cap)
driver.get("https://slack.com/signin")
signIn(driver)
selectAdaptive(driver)
driver.quit()