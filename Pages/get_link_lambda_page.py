import logging

from Locators.lamda_page_locators import LambdaPageLocators
from Pages.base_page import BasePage
from TestData.testdata import TestData
from Utils.asertion import Assertion
from Locators.link_lambda_page_locators import LocatorsLink


class LambdaLinkPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.navigate(TestData.BASE_URL_02)
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    # jira
    def get_info_jira(self):
        return self.get_text(LocatorsLink.JIRA_PRODUCT)

    def click_learn_more_Jira(self):
        self.click(LocatorsLink.LEAR_MORE_OF_JIRA)

    def verify_title_and_url_current(self, expected_title, expected_url):
        title = self.get_title()
        url_current = self.get_current_url()
        assertion = Assertion()
        assertion.assert_equal(title, expected_title)
        assertion.assert_equal(url_current, expected_url)
        self.back_browser()

    # slack
    def get_info_slack(self):
        return self.get_text(LocatorsLink.SLACK_PRODUCT)

    def click_add_to_slack(self):
        self.click(LocatorsLink.ADD_TO_SLACK_NOW)

    def verify_slack_info(self, expected_title, expected_url):
        title = self.get_title()
        url_current = self.get_current_url()
        assertion = Assertion()
        assertion.assert_equal(title, expected_title)
        assertion.assert_equal(url_current, expected_url)
        self.back_browser()

    # circle
    def get_info_circle(self):
        return self.get_text(LocatorsLink.CIRCLE_PRODUCT)

    def click_lear_more_circle(self):
        self.click(LocatorsLink.LEARN_MORE_CIRCLE)

    def verify_circle_info(self, expected_title, expected_url):
        title = self.get_title()
        url_current = self.get_current_url()
        assertion = Assertion()
        assertion.assert_equal(title, expected_title)
        assertion.assert_equal(url_current, expected_url)
        self.back_browser()

    # github
    def get_info_github(self):
        return self.get_text(LocatorsLink.GITHUB_PROJECT)

    def click_lear_more_github(self):
        self.click(LocatorsLink.LEAR_MORE_GITHUB)

    def verify_github_info(self, expected_title, expected_url):
        title = self.get_title()
        url_current = self.get_current_url()
        assertion = Assertion()
        assertion.assert_equal(title, expected_title)
        assertion.assert_equal(url_current, expected_url)
        self.back_browser()

    # gitlab

    def get_info_gitlab(self):
        return self.get_text(LocatorsLink.GITLAB_PROJECT)

    def click_lear_more_gitlab(self):
        self.click(LocatorsLink.LEAR_MORE_GITLAB)

    def verify_gitlab_info(self, expected_title, expected_url):
        title = self.get_title()
        url_current = self.get_current_url()
        assertion = Assertion()
        assertion.assert_equal(title, expected_title)
        assertion.assert_equal(url_current, expected_url)
        self.back_browser()

    # Bitbucket

    def get_info_bitbucket(self):
        return self.get_text(LocatorsLink.BITBUCKET_PROJECT)

    def click_lear_more_bitbucket(self):
        self.click(LocatorsLink.LEAR_MORE_BITBUCKET)

    def verify_bitbucket_info(self, expected_title, expected_url):
        title = self.get_title()
        url_current = self.get_current_url()
        assertion = Assertion()
        assertion.assert_equal(title, expected_title)
        assertion.assert_equal(url_current, expected_url)
        self.back_browser()

    # pay_mo
    def get_info_pay_mo(self):
        return self.get_text(LocatorsLink.PAY_MO_PROJECT)

    def click_lear_more_pay_mo(self):
        self.click(LocatorsLink.LEAR_MORE_PAY_MO)

    def verify_pay_mo_info(self, expected_title, expected_url):
        title = self.get_title()
        url_current = self.get_current_url()
        assertion = Assertion()
        assertion.assert_equal(title, expected_title)
        assertion.assert_equal(url_current, expected_url)
        self.back_browser()

    # wrike
    def get_info_wrike(self):
        return self.get_text(LocatorsLink.WRIKE_PROJECT)

    def click_lear_more_wrike(self):
        self.click(LocatorsLink.LEAR_MORE_WRIKE)

    def verify_wrike_info(self, expected_title, expected_url):
        title = self.get_title()
        url_current = self.get_current_url()
        assertion = Assertion()
        assertion.assert_equal(title, expected_title)
        assertion.assert_equal(url_current, expected_url)
        self.back_browser()

    # teamwork

    def get_info_teamwork(self):
        return self.get_text(LocatorsLink.TEAMWORK_PROJECT)

    def click_lear_more_teamwork(self):
        self.click(LocatorsLink.LEAR_MORE_TEAMWORK)

    def verify_teamwork_info(self, expected_title, expected_url):
        title = self.get_title()
        url_current = self.get_current_url()
        assertion = Assertion()
        assertion.assert_equal(title, expected_title)
        assertion.assert_equal(url_current, expected_url)
        self.back_browser()
