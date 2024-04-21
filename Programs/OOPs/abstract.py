



from abc import ABC, abstractmethod

class calculator:
    @abstractmethod
    def sum(self):
        self
    def differnce(self):
        self
    def multiply(self):
        self
    def devide(self):
        self
    

class basic_calculator(calculator):
    def __init__(self,num1, num2):
        self.num1=num1
        self.num2=num2

    def sum(self):
        print(" + ",self.num1+self.num2)
    
    def differnce(self):
        print(" - ",self.num1-self.num2)
    
    def multiply(self):
        print(" X ",self.num1*self.num2)
    
    def devide(self):
        print(" / ",self.num1/self.num2)


b = basic_calculator(20 , 10)
b.sum()
b.differnce()
b.multiply()
b.devide()
    