# How to run specific method before all the classes using fixture
import pytest

class Test1:
    def test_method1(self):
        print("method 1 called")
    
    
    def test_method2(self):
        print("method 2 called")
