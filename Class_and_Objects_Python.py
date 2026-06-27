# Class is a blueprint for creating onject
# Object is a real instance of that class
# Represent a car with basic attributes and behavior

class car:
    #__init__ is a constructor - called when an object is created
    def __init__(self,brand,model,year):
        self.brand = brand  #Instance attribute
        self.model = model
        self.year = year

    # A method - a function that belongs to the class
    def describe(self):
        return f'{self.year} {self.brand} {self.model}'
    def start_engine(self):
        return f'{self.brand} engine started'
#  Creating Objects (Instances)
car1 = car('Toyota','Corolla',2022)
car2 = car('Tesla','Model 3',2024)
print(car1.describe())
print(car1.start_engine())
print(car2.describe())
print(car2.start_engine())
print(car1.brand)
print(car1.model)
print(car1.year)
    
    
