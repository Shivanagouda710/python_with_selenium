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

# This usrl take 4 charecter to enable the sign in 
# Checking the enablity of signin button by entering 3 charecters
driver.find_element(By.ID, "user_name").send_keys("abc")
driver.find_element(By.ID, "user_pass").send_keys("abc")

is_Sign_in_Displayed=driver.find_element(By.ID, "login_button").is_displayed()
print("is_Sign_in_Displayed= ",is_Sign_in_Displayed)

is_Sign_in_Enabled=driver.find_element(By.ID, "login_button").is_enabled()
print("is_Sign_in_Enabled= ",is_Sign_in_Enabled)

is_Sign_in_Selected=driver.find_element(By.ID, "login_button").is_selected()
print("is_Sign_in_Selected= ",is_Sign_in_Selected)

time.sleep(2)

# Clearing the old username and pwd
driver.find_element(By.ID, "user_name").clear()
driver.find_element(By.ID, "user_pass").clear()


time.sleep(2)

print("---------------4 Letters -------------------")

# Again entring the userName & pwd with 4 letters 
driver.find_element(By.ID, "user_name").send_keys("abcd")
driver.find_element(By.ID, "user_pass").send_keys("abcd")

is_Sign_in_Displayed=driver.find_element(By.ID, "login_button").is_displayed()
print("is_Sign_in_Displayed= ",is_Sign_in_Displayed)

is_Sign_in_Enabled=driver.find_element(By.ID, "login_button").is_enabled()
print("is_Sign_in_Enabled= ",is_Sign_in_Enabled)

is_Sign_in_Selected=driver.find_element(By.ID, "login_button").is_selected()
print("is_Sign_in_Selected= ",is_Sign_in_Selected)

time.sleep(2)

driver.close()

