from selenium import webdriver

# Launch Chrome manually
driver = webdriver.Chrome(executable_path="path of the browser driver")

# webdriver manager library help to lauch diffrent browser automatically without manual download
# Launch Chrome
driver = webdriver.Chrome()

# Launch Edge
driver = webdriver.Edge()

# Launch Firefox
driver = webdriver.Firefox()

# Launch driver = webdriver.Safari()
driver = webdriver.Safari()

# Open a website Google
driver.get("https://www.google.com")

print(driver.title)

# Close the browser
driver.quit()
