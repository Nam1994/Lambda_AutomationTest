import unittest
from Pages.get_link_lambda_page import LambdaLinkPage
from Pages.lambda_page import LambdaPage
from TestData.testdata import TestData
from Testcases.base_test import BaseTest
from TestData.data_link import LinkData
from Utils.utility import Utility
import TestData
import allure
import pytest


class TestLamdaPage(BaseTest):
    @classmethod
    def setUp(self):
        super().setUp()

    @classmethod
    def tearDown(self):
        super().tearDown()

    def test_lambda_page(self):
        link_page = LambdaLinkPage(self.driver)
        # jira
        link_page.click_learn_more_Jira()
        link_page.verify_title_and_url_current(LinkData.TITLE_JIRA, LinkData.URL_JIRA)
        # slack
        link_page.click_add_to_slack()
        link_page.verify_slack_info(LinkData.TITLE_SLACK, LinkData.URL_SLACK)
        # Circle CL
        link_page.click_lear_more_circle()
        link_page.verify_circle_info(LinkData.TITLE_CIRCLE, LinkData.URL_CIRCLE)

        # github
        link_page.click_lear_more_github()
        link_page.verify_github_info(LinkData.TITLE_GITHUB, LinkData.URL_GITHUB)

        # gitlab
        link_page.click_lear_more_gitlab()
        link_page.verify_gitlab_info(LinkData.TITLE_GITLAB, LinkData.URL_GITLAB)

        # bitbucket
        link_page.click_lear_more_bitbucket()
        link_page.verify_bitbucket_info(LinkData.TITLE_BITBUCKET, LinkData.URL_BITBUCKET)

        # pay_mo
        link_page.click_lear_more_pay_mo()
        link_page.verify_pay_mo_info(LinkData.PAY_MO_TITLE, LinkData.PAY_MO_URL)

        # Wrike
        link_page.click_lear_more_wrike()
        link_page.verify_wrike_info(LinkData.WRIKE_TITLE, LinkData.WRIKE_URL)

        # teamwork
        link_page.click_lear_more_teamwork()
        link_page.verify_teamwork_info(LinkData.TITLE_TEAMWORK, LinkData.URL_TEAMWORK)
        csv_object = Utility()
        csv_object.read_csv('data.csv', ',')


if __name__ == "__main__":
    unittest.main()
