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

web_table=driver.find_elements(By.XPATH,'(//*[@id="product"])[2]/tbody/tr')
print("Length = ",len(web_table))

i=1
for x in web_table:
    if(x.text.__contains__("Ben")):
        print("--------",driver.find_element(By.XPATH,'(//*[@id="product"])[2]/tbody/tr/td[3]').text)
        print(x.text)
        
        
        




driver.close()

