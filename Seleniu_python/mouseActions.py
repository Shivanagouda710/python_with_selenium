from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



import time

url ="https://www.plus2net.com/javascript_tutorial/ondblclick-demo.php"
# Launch Chrome browser
driver = webdriver.Chrome()


# Navigate to a website
driver.get(url)

# maximize the window
driver.maximize_window()

time.sleep(1)

double_click_btn = driver.find_element(By.CSS_SELECTOR,"input[value='Double Click']")

action=ActionChains(driver)
action.double_click(double_click_btn).perform()

# after double click text change in box . verifying that
verify_click=driver.find_element(By.XPATH,"//div[@id='box']")
print(verify_click.text)




time.sleep(2)











driver.close()

