#############################################################################
### 	Author - Python Programmer                               ############
###		Description - Python Module                              ############
### 	Date - 23-09-2023                                        ############
###																 ############
#############################################################################

#calculator  +,-,/,*   sum,sub,multiply,divide are known as user defined function 

#Sum function defination 
def sum(a,b) :
    add = a + b 
    return add 

#SuB function defination 
def sub(a,b) :
    sub1 = a - b 
    return sub1
    
#Multiply function defination 
def multiply(a,b) :
    mul = a * b 
    return mul

#Divide function defination 
def divide(a,b) :
    div = a / b 
    return div

def printcalc():
    print("Calcuation functions")

def numberofelelist(list) :
    length = 0 
    for count in list :
        length = length + 1 
    print("Length of list ",length)

PI = 3.14 