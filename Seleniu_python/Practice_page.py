from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

import time
url ="https://www.rahulshettyacademy.com/AutomationPractice/"
# Launch Chrome browser
driver = webdriver.Chrome()

driver.get(url)
driver.maximize_window()

print("Title = "+driver.title)
print("Title = "+driver.current_url)

radioText = driver.find_element(By.ID,"radio-btn-example")

print("-------",radioText.text)

radioOptions=driver.find_elements(By.CLASS_NAME,"radioButton")
print("Number of radio buttons ",len(radioOptions))

for x in radioOptions:
    x.click()
    time.sleep(3)


textInput =driver.find_element(By.ID,"autocomplete")
textInput.send_keys("My self shiva")
time.sleep(2)

dropId=driver.find_element(By.ID,"dropdown-class-example")
dropOption = Select(dropId)

dropOption.select_by_value("option1")
time.sleep(2)
dropOption.select_by_value("option2")
time.sleep(2)
dropOption.select_by_value("option3")
time.sleep(2)

print("*************** Checkbox ******************")
checkbox=driver.find_elements(By.XPATH,'//*[contains(@id,"checkBoxOption")]')
print("Number of checkbox = ",len(checkbox))

for x in checkbox:
    x.click()
    time.sleep(2)


driver.close()

