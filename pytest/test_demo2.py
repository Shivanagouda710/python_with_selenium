# How to run specific method before all the classes using fixture
import pytest

class Test2:
    def test_method3(self):
        print("method 3 called")
    
    
    def test_method4(self):
        print("method 4 called")
