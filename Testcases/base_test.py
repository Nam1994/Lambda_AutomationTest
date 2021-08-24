import os
import unittest
from selenium import webdriver
from TestData.testdata import TestData


class BaseTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        browser = self.getBrowser()
        print('browser', browser)
        self.driver = self.launchBrowser(browser)
        self.driver.maximize_window()

    @classmethod
    def tearDown(self):
        self.driver.quit()

    @staticmethod
    def launchBrowser(browserName='chrome'):
        try:
            if browserName.lower() == 'firefox':
                return webdriver.Firefox()
            elif browserName.lower() == 'firefox':
                return webdriver.Ie()
            else:
                return webdriver.Chrome()
        except Exception as msg:
            print("Launch Browser: %s" % str(msg))

    @staticmethod
    def getBrowser():
        try:
            return os.environ['BROWSER_NAME']
        except:
            return TestData.BROWSER_NAME
