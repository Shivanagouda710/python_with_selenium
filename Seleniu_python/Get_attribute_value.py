from selenium import webdriver
from selenium.webdriver.common.by import By

import time

url ="https://www.rahulshettyacademy.com/AutomationPractice/"
# Launch Chrome browser
driver = webdriver.Chrome()

# Navigate to a website
driver.get(url)

# maximize the window
driver.maximize_window()

# Getting diffrent attributes for particular element
attr1 =driver.find_element(By.XPATH, "//input[@id='confirmbtn']").get_attribute("value")
print(attr1)

attr2 =driver.find_element(By.XPATH, "//input[@id='confirmbtn']").get_attribute("id")
print(attr2)

attr3 =driver.find_element(By.XPATH, "//input[@id='confirmbtn']").get_attribute("class")
print(attr3)






time.sleep(1)

driver.close()

