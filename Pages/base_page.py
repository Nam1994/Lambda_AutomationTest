import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    def navigate(self, url):
        message = "Navigate to '{}'"
        logging.info(message.format(url))
        self.driver.implicitly_wait(self.timeout)
        self.driver.get(url)

    def get_title(self):
        logging.info('Get current title')
        return self.driver.title

    def get_current_url(self):
        logging.info('Get current url')
        return self.driver.current_url

    def get_property(self, by_locator, attribute):
        message = "Get property '{}' of locator '{}'"
        logging.info(message.format(attribute, ','.join(by_locator)))

        element = WebDriverWait(self.driver, self.timeout). \
            until(EC.visibility_of_element_located(by_locator))

        return element.get_property(attribute)

    def execute_script(self, script):
        message = "Execute the scripts: '{}'"
        logging.info(message.format(script))
        self.driver.execute_script(script)

    def move_to_element(self, by_locator):
        message = "Move to the element with locator '{}'"
        logging.info(message.format(','.join(by_locator)))

        actions = ActionChains(self.driver)
        element = WebDriverWait(self.driver, self.timeout). \
            until(EC.visibility_of_element_located(by_locator))

        actions.move_to_element(element).perform()

    def switch_to_window(self, index=0):
        message = "Switch to window with the index = {}"
        logging.info(message.format(index))
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[index])

    def count_windows(self):
        logging.info('Count total windows')
        try:
            window_handles = self.driver.window_handles
            total = len(window_handles)
            return total
        except Exception as ex:
            return 0

    def close_window(self):
        logging.info('Close window')
        try:
            self.driver.close()
            self.switch_to_window(0)
        except Exception as ex:
            logging.error("Close Window: %s" % str(ex))

    def click(self, by_locator):
        message = "Click on the element with locator '{}'"
        logging.info(message.format(','.join(by_locator)))

        element = WebDriverWait(self.driver, self.timeout). \
            until(EC.visibility_of_element_located(by_locator))
        element.click()

    def back_browser(self):
        logging.info('Back browser')
        self.driver.back()

    def get_text(self, by_locator):
        message = "Get text of the element with locator '{}'"
        logging.info(message.format(','.join(by_locator)))

        element = WebDriverWait(self.driver, self.timeout). \
            until(EC.visibility_of_element_located(by_locator))
        return element.text
