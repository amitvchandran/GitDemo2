# creation of class
# Self keyword is mandatory for calling variable names into method
# instance and class variable has whole different purpose
# constructor name should be __init__
# new keyword is not required when u create new object


class Calculator:
    num = 100 # class variable

    # This one is default constructor in python
    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when objet is created")

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


# always create object outside the class to call them
obj = Calculator(2,3)  #Syntax to create new object in python
obj.getData()
print(obj.Summation())

obj1 = Calculator(4, 5)  #Syntax to create new object in python
obj1.getData()
print(obj1.Summation())