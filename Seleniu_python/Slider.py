from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



import time

url ="https://demo.automationtesting.in/Slider.html"
# Launch Chrome browser
driver = webdriver.Chrome()


# Navigate to a website
driver.get(url)

# maximize the window
driver.maximize_window()

time.sleep(1)
slider = driver.find_element(By.XPATH,"(//a[@class='ui-slider-handle ui-state-default ui-corner-all'])[1]")

action=ActionChains(driver)
action.click_and_hold(slider).move_by_offset(50,0).pause(2).move_by_offset(100,1).perform()








time.sleep(2)











driver.close()

