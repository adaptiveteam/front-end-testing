from unittest import TestCase
import os
import logging
import urllib3
import certifi
import components
from selenium import webdriver
from sauceclient import SauceClient


class TestSetUp(TestCase):
    drivers = {}
    sauce_username = os.environ['SAUCE_USERNAME']
    sauce_access_key = os.environ['SAUCE_ACCESS_KEY']
    remote_url = os.environ['REMOTE_URL']

    def get_driver(self, scenario, site_to_test):
        rv = None
        desired_cap = {
            'platform': os.environ['PLATFORM'],
            'browserName': os.environ['BROWSER'],
            'version': os.environ['BROWSER_VERSION'],
            'build': "none",
            'name': scenario,
            'username': os.environ['SAUCE_USERNAME'],
            'accessKey': os.environ['SAUCE_ACCESS_KEY'],
        }
        if scenario not in self.drivers.keys():
            try:
                self.drivers[scenario] = webdriver.Remote(command_executor=self.remote_url,
                                                          desired_capabilities=desired_cap)
                self.drivers[scenario].get(site_to_test)
                rv = self.drivers[scenario]
            except Exception as e:
                logging.error(e)
                rv = None
        return rv


    @classmethod
    def setUpClass(cls):
        cls.http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        cls.sauce_client = SauceClient(cls.sauce_username, cls.sauce_access_key)

    @classmethod
    def tearDownClass(cls):
        for driver in cls.drivers.values():
            driver.quit()

    def test_set_up(self):
        scenario = "setup"
        driver = self.get_driver(scenario, os.environ["SITE_TO_TEST"])
        result = "failed"
        try:
            components.sign_in(driver, os.environ['WORKSPACE'], os.environ['USER_EMAIL'], os.environ['USER_PASSWORD'])
            driver.implicitly_wait(5)
            components.select_adaptive(driver)
            result = "passed"
        except Exception as e:
            logging.error(e)

        self.sauce_client.jobs.update_job(driver.session_id, passed=result, name=scenario)
