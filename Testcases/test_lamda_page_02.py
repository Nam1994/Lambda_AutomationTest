import unittest

from Pages.lambda_page import LambdaPage
from TestData.testdata import TestData
from Testcases.base_test import BaseTest


class TestLamdaPage(BaseTest):
    @classmethod
    def setUp(self):
        super().setUp()

    @classmethod
    def tearDown(self):
        super().tearDown()

    def test_lamda_page(self):
        lambda_page = LambdaPage(self.driver)
        lambda_page.move_to_all_integrations_link()
        href_prop = lambda_page.get_all_integrations_link_property()

        lambda_page.execute_script('window.open("' + href_prop + '");')
        lambda_page.switch_to_window(1)
        # Verify URL
        lambda_page.verify_url(href_prop)

        lambda_page.move_to_codeless_automation_link()
        lambda_page.click_testingwhiz_integration_link()

        # Verify Title
        lambda_page.verify_title(TestData.TITLE_TESTING_WHIZ_INTEGRATION)

        lambda_page.close_window()


        # Verify total windows
        lambda_page.verify_total_windows(1)

        lambda_page.navigate(TestData.BLOG_URL)
        lambda_page.click_community_link()

        # Verify URL
        lambda_page.verify_url(TestData.COMMUNITY_URL)


if __name__ == "__main__":
    unittest.main()
