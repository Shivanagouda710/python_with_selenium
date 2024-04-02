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


header1 =driver.find_element(By.XPATH, "//h1")
print(header1.text)






time.sleep(1)

driver.close()

