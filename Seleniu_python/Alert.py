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

time.sleep(1)

alert_title = driver.find_element(By.XPATH,"//legend[normalize-space()='Switch To Alert Example']")
print("alert title ",alert_title.text)

# click on alert button
driver.find_element(By.ID,"alertbtn").click()

# siwching to alert and getting a text 
print("alert text = ",driver.switch_to.alert.text)

# accepting the alert
driver.switch_to.alert.accept()

time.sleep(2)


#click on conform button
driver.find_element(By.ID,"confirmbtn").click()


# two option 1 ok , 2 cancel here we are clicking on cancel
driver.switch_to.alert.dismiss()





time.sleep(2)











driver.close()

