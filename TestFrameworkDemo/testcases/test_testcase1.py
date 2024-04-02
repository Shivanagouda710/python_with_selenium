from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import pytest

from pages.launch import LaunchPage

# from ..pages.launch import LaunchPage
# from ..pages.launch import LaunchPage



@pytest.mark.usefixtures("setup")
class Testdemo():
    def test_search(self):
        l=LaunchPage(self.driver)
        l.test_getElement()






