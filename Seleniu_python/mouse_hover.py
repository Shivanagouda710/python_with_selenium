from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



import time

url ="https://www.yatra.com/"
# Launch Chrome browser
driver = webdriver.Chrome()


# Navigate to a website
driver.get(url)

# maximize the window
driver.maximize_window()

time.sleep(1)

more_option = driver.find_element(By.CSS_SELECTOR,".more-arr")

action=ActionChains(driver)
action.move_to_element(more_option).perform()





time.sleep(2)











driver.close()

