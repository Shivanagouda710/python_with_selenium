from selenium import webdriver
from selenium.webdriver.common.by import By

import time

url ="https://training.openspan.com/login#:~:text=Sign%20In%20%7C%20Pega%20Studio%20Training,organization's%20network%20or%20personal%20accounts."
# Launch Chrome browser
driver = webdriver.Chrome()

# Navigate to a website
driver.get(url)

# maximize the window
driver.maximize_window()



driver.find_element(By.ID, "user_name").send_keys("abcd")
driver.find_element(By.ID, "user_pass").send_keys("abcd")

# Particular element screenshot
is_Sign_in_Displayed=driver.find_element(By.ID, "login_button")
is_Sign_in_Displayed.screenshot("Sign_in.png")

#Full screenshot 
driver.get_screenshot_as_file("Full_screen.png")


time.sleep(1)

driver.close()

