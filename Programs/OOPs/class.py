

# class is a collection of objects
# Object  is entity that has state and behavior
# _ _init_ _ method is constructor
# automatically called when a new instance of a class is created
# initializing the attributes of the newly created object
# he __init__ method always takes a single argument named self


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age = age

    
    def display(self):
        print("My name is ",self.name," and age is ",self.age)



p = Person("sachin",27)
p2 = Person("stark",20)
p.display()
p2.display()