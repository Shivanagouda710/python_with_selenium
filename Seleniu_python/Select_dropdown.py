from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.select import Select
import time

url ="https://www.rahulshettyacademy.com/AutomationPractice/"
# Launch Chrome browser
driver = webdriver.Chrome()

# Navigate to a website
driver.get(url)

# maximize the window
driver.maximize_window()


dropdown = driver.find_element(By.ID,"dropdown-class-example")

drpselect=Select(dropdown)
drpselect.select_by_index(1)
time.sleep(2)
drpselect.select_by_visible_text("Option2")

# time.sleep(2)
drpselect.select_by_value("option3")


time.sleep(1)

driver.close()

