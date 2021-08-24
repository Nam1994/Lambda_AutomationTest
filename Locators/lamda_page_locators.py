
from selenium.webdriver.common.by import By


class LambdaPageLocators(object):
    TXT_ALL_INTEGRATIONS = (By.XPATH, "//a[text()='See All Integrations']")
    TXT_CODELESS_AUTOMATION = (By.XPATH, "//a[text()='Codeless Automation']")
    LINK_TESTING_WHIZ = (By.XPATH, "//a[contains(@href,'testingwhiz-integration/') and text()='Learn More']")
    TXT_COMMUNITY = (By.XPATH, "(//a[text()='Community'])[2]")
