PI = 3.14
import math 

def add(a,b):
    result = a+b
    return result 

class Person : #common noun - class 

    def __init__(self,name,age,gender):
        self.name = name 
        self.age = age 
        self.gender = gender 
    def persondetails(self):
        print("Person name is ",self.name,self.age,self.gender)
        
    def sleeping(self):
        print(self.name,"is sleeping")
    
    

class Math :
        
    def __init__(self,num1,num2):
        self.num1 = num1 
        self.num2 = num2 
        
    def add(self):
        self.result = self.num1 + self.num2
        print("Sum of two number ",self.result)

    def sub(self):
        self.result = self.num1 - self.num2
        print("Subtraction of two number ",self.result)
        
    def mul(self,num1,num2,num3):
        self.result = num1 * num2 * num3
        return self.result
        
    def divide(self):
        self.result = self.num1 / self.num2
        return self.result
        

        
        
