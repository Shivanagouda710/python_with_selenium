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

# Select From text box
driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']").click()
time.sleep(3)


country_to_select = "New York (LGA)"
# Enter the 3 letters
driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']").send_keys("New") # New Gives list

time.sleep(3)

from_List = driver.find_elements(By.CLASS_NAME,"ac_cityname")
print("Number of country = ",len(from_List))

for x in from_List:
    print(x.text)
    if(country_to_select==x.text):
        print("Found country = ",x.text)
        x.click()  # Selected the Given country
        break













time.sleep(3)

driver.close()

