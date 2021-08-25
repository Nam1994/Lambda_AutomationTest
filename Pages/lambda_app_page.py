import logging

from Locators.lamda_page_locators import LambdaPageLocators
from Pages.base_page import BasePage
from TestData.testdata import TestData
from Utils.asertion import Assertion
from Locators.integration_page_locators import LocatorsApp
from Objects.app_object import Object


class LambdaAppPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.navigate(TestData.BASE_URL_02)
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    def click_app_in_lambda(self, index):
        list_title = []
        for index in range(1, 10):
            self.click(LocatorsApp.learn_more_app(index))
            title = self.get_title()
            url = self.get_current_url()
            object = Object(title, url)
            list_title.append(object)
            self.back_browser()
        return list_title

    def compare_info_app(self, expected, actual):
        assertion = Assertion()
        assertion.assertEqual(expected.title, actual.title, 'The title not match')
