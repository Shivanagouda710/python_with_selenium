from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




import time

url ="https://www.hyrtutorials.com/p/waits-demo.html"
# Launch Chrome browser
driver = webdriver.Chrome()


# Navigate to a website
driver.get(url)

# maximize the window
driver.maximize_window()

time.sleep(1)
print("Website title",driver.title)


outside_element=driver.find_element(By.XPATH,"//h1[normalize-space()='Waits Demo']")
print("outside_element = ",outside_element.text)

btn1=driver.find_element(By.ID,"btn1")
btn1.click()

# time.sleep(6) # button to visible takes 5 sec. so hardcoding 

driver.implicitly_wait(time_to_wait=10) # time unit in seconds
txt1_verify=driver.find_element(By.ID,"txt1")
print(txt1_verify.is_displayed())


btn2=driver.find_element(By.ID,"btn2")
btn2.click()

# time.sleep(6) # button to visible takes 5 sec. so hardcoding 

# below using explicit wait
wait =  WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.ID,"txt2"))) # element 2 takes 10 min to get visible 
# txt1_verify=driver.find_element(By.ID,"txt2")
print("Displayed = ",driver.find_element(By.ID,"txt2").is_displayed())

# Rereshing the browser to check fluent wait
driver.refresh()

# once after refresh privious session will be closed so again we need to define an element
btn2=driver.find_element(By.ID,"btn2")
btn2.click()


# Fluent wait only one change from explicit wait that is last argument polling time
wait1 =  WebDriverWait(driver,10,poll_frequency=5)
wait1.until(EC.visibility_of_element_located((By.ID,"txt2"))) # element 2 takes 10 min to get visible 















time.sleep(2)











driver.close()

