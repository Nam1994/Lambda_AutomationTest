import unittest
from Pages.lambda_app_page import LambdaAppPage
from Pages.lambda_page import LambdaPage
from TestData.testdata import TestData
from Testcases.base_test import BaseTest
from TestData.data_link import LinkData
from Utils.utility import Utility
import TestData
import allure
import pytest
import csv


class TestLambdaAppPage(BaseTest):
    @classmethod
    def setUp(self):
        super().setUp()

    @classmethod
    def tearDown(self):
        super().tearDown()

    def test_lambda_page(self):
        app_page = LambdaAppPage(self.driver)
        #b = app_page.click_app_in_lambda()
        #for index in range(0, len(b)):
            #print(b[index])
        print('----------------------------')
        utility = Utility()
        a = utility.read_csv('C:\\Users\\Admin\\Desktop\\Python Selenium\\LamdaTest_Mr.Khanh\\TestData\\data.csv')
        for index in range(1, len(a)):
            app_page.compare_info_app(a[index], app_page.click_app_in_lambda()[index])





if __name__ == "__main__":
    unittest.main()
