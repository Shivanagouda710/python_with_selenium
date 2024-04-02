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

# Select Rediobutton 1 
# driver.find_element(By.NAME, "radioButton1").click()

# Slecting multiple radio button in Dinamic way
check_Redio_btn=driver.find_elements(By.XPATH,"//*[starts-with(@name,'radioButton')]") 
print("Number of radio button  = ",len(check_Redio_btn))

for i in check_Redio_btn:
    i.click()
    time.sleep(2)
    print(f"element {i} enabled = ",i.is_enabled())










time.sleep(1)

driver.close()

