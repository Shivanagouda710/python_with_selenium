
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

url ="https://www.rahulshettyacademy.com/AutomationPractice/"
# Launch Chrome browser
driver = webdriver.Chrome()
driver.get(url)


driver.maximize_window

radio1 = driver.find_element(By.XPATH,'(//*[@name="radioButton"])[1]')

radio1.click()
time.sleep(2)

radio2 = driver.find_element(By.XPATH,'(//*[@name="radioButton"])[2]')

radio2.click()

time.sleep(2)

driver.find_element(By.ID,"autocomplete").send_keys("india")
time.sleep(2)



checkbox1 = driver.find_element(By.ID,"checkBoxOption1")
checkbox1.click()

time.sleep(2)

checkbox2 = driver.find_element(By.ID,"checkBoxOption2")
checkbox2.click()
time.sleep(2)

print("Text == ",driver.find_element(By.XPATH,'//*[contains(text(),"Dropdown Example")]').text)


dropdownid= driver.find_element(By.ID,"dropdown-class-example")




driver.close