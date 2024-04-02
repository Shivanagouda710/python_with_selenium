from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



import time

url ="https://demo.automationtesting.in/Static.html"
# Launch Chrome browser
driver = webdriver.Chrome()


# Navigate to a website
driver.get(url)

# maximize the window
driver.maximize_window()

time.sleep(1)
ele1=driver.find_element(By.ID,"angular")
ele2=driver.find_element(By.ID,"mongo")
ele3=driver.find_element(By.ID,"node")

drop_destination = driver.find_element(By.ID,"droparea")



action=ActionChains(driver)

#method 1. scroll to the element first and draga and drop to destination area 
# action.scroll_to_element(ele1).drag_and_drop(ele1,drop_destination).perform()

# method2. one by one element draga and drop to destination area
# action.drag_and_drop(ele1,drop_destination).perform()
# time.sleep(2)
# action.drag_and_drop(ele2,drop_destination).perform()
# time.sleep(2)
# action.drag_and_drop(ele3,drop_destination).perform()

# method3. all elements in sigle chain

action.scroll_to_element(ele1).drag_and_drop(ele1,drop_destination).scroll_to_element(ele2).drag_and_drop(ele2,drop_destination).scroll_to_element(ele3).drag_and_drop(ele3,drop_destination).perform()





time.sleep(2)











driver.close()

