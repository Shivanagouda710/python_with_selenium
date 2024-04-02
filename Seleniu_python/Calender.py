from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import time

url ="https://www.yatra.com/"
# Launch Chrome browser
driver = webdriver.Chrome()


# Navigate to a website
driver.get(url)

# maximize the window
driver.maximize_window()

# Select From text box
driver.find_element(By.ID, "BE_flight_origin_date").click()

time.sleep(2)
driver.find_element(By.ID, "02/04/2024").click()



time.sleep(2)
ele = driver.find_element(By.ID, "04/02/2025").click()


time.sleep(3)













time.sleep(3)

driver.close()

