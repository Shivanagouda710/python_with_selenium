from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



import time

url ="https://swisnl.github.io/jQuery-contextMenu/demo.html"
# Launch Chrome browser
driver = webdriver.Chrome()


# Navigate to a website
driver.get(url)

# maximize the window
driver.maximize_window()

time.sleep(1)

right_clcik_me_btn = driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")

action=ActionChains(driver)
action.move_to_element(right_clcik_me_btn).context_click().perform()






time.sleep(2)











driver.close()

