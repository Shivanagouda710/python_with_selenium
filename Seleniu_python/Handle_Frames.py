from selenium import webdriver
from selenium.webdriver.common.by import By


import time

url ="https://www.rahulshettyacademy.com/AutomationPractice/"
# Launch Chrome browser
driver = webdriver.Chrome()


# Navigate to a website
driver.get(url)

# maximize the window
driver.maximize_window()

time.sleep(1)

outside_frame =driver.find_element(By.XPATH,"//legend[normalize-space()='iFrame Example']")
print("outside_frame = ",outside_frame.text)

number_of_frames=driver.find_element(By.TAG_NAME,"iframe")
print("number of frames = ",number_of_frames)

frame_id =driver.find_element(By.XPATH,"//iframe[@id='courses-iframe']")
print("frame id = ",frame_id)
driver.switch_to.frame(frame_id)


print("After switching.....")

inside_frame = driver.find_element(By.XPATH,"//li[normalize-space()='contact@rahulshettyacademy.com']")
print("inside_frame = ",inside_frame.text)

time.sleep(2)











driver.close()

