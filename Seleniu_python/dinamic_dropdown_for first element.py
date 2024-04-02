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
driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']").click()

# Enter the 3 letters
driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']").send_keys("DEL") # DEL is code for New Delhi 

# Hit enter to select the first option
driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']").send_keys(Keys.ENTER)










time.sleep(1)

driver.close()

