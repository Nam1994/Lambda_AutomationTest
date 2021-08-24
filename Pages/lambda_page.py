import logging

from Locators.lamda_page_locators import LambdaPageLocators
from Pages.base_page import BasePage
from TestData.testdata import TestData
from Utils.asertion import Assertion


class LambdaPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.navigate(TestData.BASE_URL)
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    def move_to_all_integrations_link(self):
        self.move_to_element(LambdaPageLocators.TXT_ALL_INTEGRATIONS)

    def get_all_integrations_link_property(self):
        return self.get_property(LambdaPageLocators.TXT_ALL_INTEGRATIONS, 'href')

    def move_to_codeless_automation_link(self):
        self.move_to_element(LambdaPageLocators.TXT_CODELESS_AUTOMATION)

    def click_testingwhiz_integration_link(self):
        self.click(LambdaPageLocators.LINK_TESTING_WHIZ)

    def click_community_link(self):
        self.click(LambdaPageLocators.TXT_COMMUNITY)

    def verify_title(self, expected):
        title = self.get_title()
        assertion = Assertion()
        assertion.assert_equal(title, expected)

    def verify_url(self, expected):
        url = self.get_current_url()
        assertion = Assertion()
        assertion.assert_equal(url, expected)

    def verify_total_windows(self, expected):
        total = self.count_windows()
        assertion = Assertion()
        assertion.assert_equal(total, expected)
