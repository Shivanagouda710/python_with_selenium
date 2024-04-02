from selenium.webdriver.common.by import By

class LaunchPage():
    def __init__(self,driver):
        self.driver=driver


    def test_getElement(self):
        ele = self.driver.find_element(By.XPATH, "//h1")
        print("++++++++",ele.text)
        assert ele.text == "Practice Page"




