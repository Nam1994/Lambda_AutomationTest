from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.lambdatest.com/')
driver.implicitly_wait(10)

element = driver.find_element(By.XPATH, "//a[contains(text(),'See All Integrations')]")

actions = ActionChains(driver)
actions.move_to_element(element).perform()

# Or
# driver.execute_script("arguments[0].scrollIntoView();", element)

# element.click()
integrations_href = element.get_property('href')



driver.execute_script('window.open("' + integrations_href + '");')

window_handles = driver.window_handles
print(window_handles)
driver.switch_to.window(window_handles[1])


print(integrations_href)
print(driver.current_url)

assert integrations_href == driver.current_url

element = driver.find_element(By.XPATH, "//a[text()='Codeless Automation']")

actions = ActionChains(driver)
actions.move_to_element(element).perform()

testingwhiz_link = driver.find_element(By.XPATH, "//a[contains(@href,'testingwhiz-integration') and text()='Learn More']")
testingwhiz_link.click()
print(driver.title)

assert 'TestingWhiz Integration | LambdaTest' == driver.title
driver.close()


multi_window = driver.window_handles
driver.switch_to.window(multi_window[0])
length = len(multi_window)
print("Number of window open: ", length)

driver.get('https://www.lambdatest.com/blog')
community_link = driver.find_element(By.XPATH, "(//a[contains(@href,'community') and text()='Community'])[2]")
community_link.click()

assert 'https://community.lambdatest.com/' == driver.current_url

driver.quit()
