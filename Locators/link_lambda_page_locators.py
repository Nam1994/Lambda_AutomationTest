from selenium import webdriver
from selenium.webdriver.common.by import By


class LocatorsLink(object):
    """REGISTER_NOW = (By.XPATH, "//a[text()='Register Now']")
    LAMBDA_TEST_LOGO = (By.XPATH, "//div[@class='flex justify-between items-center']")
    LIVE = (By.XPATH, "//a[text()='Live']")
    AUTOMATION_MENU = (By.XPATH, "(//a[text()='Automation'])[1]")
    PRICING = (By.XPATH, "//a[text()='Pricing']")
    BUTTON_RESOURCES = (By.XPATH, "//button[text()='Resources ']")
    BLOG_RESOURCES = (By.XPATH, "//ul/a[text()='Blog']")
    SUPPORT = (By.XPATH, "//a[text()='Support']")
    LOGIN = (By.XPATH, "//a[text()='Login']")
    START_FREE_TESTING = (By.XPATH, "//a[text()='Start Free Testing']")
    AUTOMATION_TESTING = (By.XPATH, "(//div[@class='thumb-titel'])[text()='Automated Testing']")"""



    # jira
    LEARN_MORE_OF_AUTOMATION = (By.XPATH, "(//div[@class='owl-thumb-content'])[1]//a[text()='Learn more ']")
    JIRA_PRODUCT = (By.XPATH, "(//div[@id='popular_row']//ancestor::div[@class='mt-10 p-30 integrations_box border border-black relative rounded'])[1]")

    LEAR_MORE_OF_JIRA = (By.XPATH, "((//div[@id='popular_row'])//a[text()='Learn More'])[1]")

    # Slack
    SLACK_PRODUCT = (By.XPATH, "(//div[@id='popular_row']//ancestor::div[@class='mt-10 p-30 integrations_box border border-black relative rounded'])[2]")
    ADD_TO_SLACK_NOW = (By.XPATH, "((//div[@id='popular_row'])//a[text()='Add to Slack Now'])[1]")

    # circle cl
    CIRCLE_PRODUCT = (By.XPATH,
                     "(//div[@id='popular_row']//ancestor::div[@class='mt-10 p-30 integrations_box border border-black relative rounded'])[3]")
    LEARN_MORE_CIRCLE = (By.XPATH, "((//div[@id='popular_row'])//a[text()='Learn More'])[2]")

    # Github
    GITHUB_PROJECT = (By.XPATH, "(//div[@id='project_row']//ancestor::div[@class='mt-10 p-30 integrations_box border border-black relative rounded'])[1]")
    LEAR_MORE_GITHUB = (By.XPATH, "((//div[@id='project_row'])//a[text()='Learn More'])[1]")

    # GitLab
    GITLAB_PROJECT = (By.XPATH,
                      "(//div[@id='project_row']//ancestor::div[@class='mt-10 p-30 integrations_box border border-black relative rounded'])[2]")
    LEAR_MORE_GITLAB = (By.XPATH, "((//div[@id='project_row'])//a[text()='Learn More'])[2]")

    # Bitbucket
    BITBUCKET_PROJECT = (By.XPATH,
                      "(//div[@id='project_row']//ancestor::div[@class='mt-10 p-30 integrations_box border border-black relative rounded'])[3]")
    LEAR_MORE_BITBUCKET = (By.XPATH, "((//div[@id='project_row'])//a[text()='Learn More'])[3]")

    #paymo
    PAY_MO_PROJECT = (By.XPATH,
                         "(//div[@id='project_row']//ancestor::div[@class='mt-10 p-30 integrations_box border border-black relative rounded'])[4]")
    LEAR_MORE_PAY_MO = (By.XPATH, "((//div[@id='project_row'])//a[text()='Learn More'])[4]")

    # team work
    TEAMWORK_PROJECT = (By.XPATH,
                      "(//div[@id='project_row']//ancestor::div[@class='mt-10 p-30 integrations_box border border-black relative rounded'])[7]")
    LEAR_MORE_TEAMWORK = (By.XPATH, "((//div[@id='project_row'])//a[text()='Learn More'])[7]")

    # WRIKE
    WRIKE_PROJECT = (By.XPATH,
                        "(//div[@id='project_row']//ancestor::div[@class='mt-10 p-30 integrations_box border border-black relative rounded'])[9]")
    LEAR_MORE_WRIKE = (By.XPATH, "((//div[@id='project_row'])//a[text()='Learn More'])[8]")

    # Asana
    ASANA_PROJECT = (By.XPATH,
                     "(//div[@id='project_row']//ancestor::div[@class='mt-10 p-30 integrations_box border border-black relative rounded'])[9]")
    LEAR_MORE_ASANA = (By.XPATH, "((//div[@id='project_row'])//a[text()='Learn More'])[9]")
