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

# current parent window
parent_window= driver.current_window_handle

print("parent window = ",parent_window)

# Click on link whcih open other window
driver.find_element(By.XPATH,"(//img[@class='conta iner large-banner'])[1]").click()

# storing all opened window id's
windows=driver.window_handles

# looping through the chil windows till child window matches
for child_window in windows:
    if(child_window!=parent_window):
        driver.switch_to.window(child_window)
        time.sleep(3)
        break

# Once after swiching validating a element from the child window
child_window_text = driver.find_element(By.CLASS_NAME,"main-title")
print(child_window_text.text)

# closing the chil window
driver.close()
time.sleep(3)


# swiching to parent window
driver.switch_to.window(parent_window)
time.sleep(3)


# Once after swiching to parent window  validating a element from the parent window
parent_window_text = driver.find_element(By.XPATH,"//h1[@class='main-heading']")
print(parent_window_text.text)

time.sleep(3)



# closing current window
driver.close()

