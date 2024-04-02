import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



@pytest.fixture(scope="class")
def setup(request):
    url = "https://www.rahulshettyacademy.com/AutomationPractice/"
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver  # Setting driver on the test class
    yield
    driver.close()