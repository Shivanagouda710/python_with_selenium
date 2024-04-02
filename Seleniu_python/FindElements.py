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
links =driver.find_elements(By.TAG_NAME, "a")
# how many links woth tagName  a 
print(len(links)) # 27 

for x in links:
    print(x.text)  # Text related to particular element



time.sleep(1)

driver.close()

