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

parent_window=driver.current_window_handle
print("parent winodow = ",parent_window)

openwindow_id=driver.find_element(By.ID,"openwindow")
openwindow_id.click()

windowHandles=driver.window_handles
print("Number of opened window  =",len(windowHandles))
print(windowHandles)


# for x in windowHandles:
#     driver.switch_to.window(x)
#     print(driver.title)
#     if((driver.title).__contains__("QAClick Academy")):
#         print("Found")
#         driver.close()        


# print("************************************")
# driver.switch_to.parent_frame()

# print(driver.current_url)

# Iterate over each window handle
for window_handle in windowHandles:
    # Switch to the window
    driver.switch_to.window(window_handle)
    # Check if the title contains "QAClick Academy"
    if "QAClick Academy" in driver.title:
        print("Found")
        # Close the window
        driver.close()

# Switch back to the parent window
driver.switch_to.window(parent_window)

# Now you're back in the parent window
print(driver.current_url)


# --------------------------------------------
opentab_button=driver.find_element(By.ID,"opentab")
opentab_button.click()
openTab=driver.window_handles
print("Number of opened window  =",len(openTab))
print(openTab)


for x in openTab:
    driver.switch_to.window(x)
    print(driver.title)
    if((driver.title).__contains__("QAClick Academy")):
        print("Found")
        # driver.close()
        

driver.switch_to.window(parent_window)

time.sleep(5)

print(driver.current_url)

driver.find_element(By.ID,"name").send_keys("sachin")



alertConform= driver.find_element(By.ID,"confirmbtn")
alertConform.click()

driver.switch_to.alert.dismiss()
alertConform.click()
time.sleep(3)
driver.switch_to.alert.accept()


time.sleep(5)
driver.close()