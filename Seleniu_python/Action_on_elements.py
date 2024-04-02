from selenium import webdriver
from selenium.webdriver.common.by import By

import time

url ="https://www.rahulshettyacademy.com/AutomationPractice/"
# Launch Chrome browser
driver = webdriver.Chrome()

# Navigate to a website
driver.get(url)

print(driver.title)

# using xpath
header1 =driver.find_element(By.XPATH, "//h1")

# using Css selector
header2 =driver.find_element(By.CSS_SELECTOR, "body h1")



print(header1.text)
print(header2.text)

time.sleep(1)

driver.close()

