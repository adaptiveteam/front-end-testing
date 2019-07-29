from unittest import TestCase
import os
import scenarios
import urllib3
import certifi
from selenium import webdriver
import tracemalloc

tracemalloc.start()

class TestSet_up(TestCase):
    def get_desired_capabilities(self, name):
        desired_cap = {
            'platform': os.environ['PLATFORM'],
            'browserName': os.environ['BROWSER'],
            'version': os.environ['BROWSER_VERSION'],
            'build': "none",
            'name': name,
            'username': os.environ['SAUCE_USERNAME'],
            'accessKey': os.environ['SAUCE_ACCESS_KEY'],
        }
        return desired_cap

    def setUp(self):
        desired_cap = self.get_desired_capabilities('Log-In and Set-Up')
        self.http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        self.driver = webdriver.Remote(command_executor=os.environ['REMOTE_URL'], desired_capabilities=desired_cap)
        self.driver.get(os.environ['SITE_TO_TEST'])


    def tearDown(self):
        self.driver.quit()


    def test_set_up(self):
        scenarios.set_up(self.driver)
        return True

