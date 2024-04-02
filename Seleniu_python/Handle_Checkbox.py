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

# Select checkbox 1 
# driver.find_element(By.ID, "checkBoxOption1").click()

# Slecting multiple check box in Dinamic way
check_boxs=driver.find_elements(By.XPATH,"//*[starts-with(@id,'checkBoxOption')]") 
print("Number of checkbox  = ",len(check_boxs))

for i in check_boxs:
    i.click()
    time.sleep(2)
    print(f"element {i} enabled = ",i.is_enabled())










time.sleep(1)

driver.close()

