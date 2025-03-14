#############################################################################
### 	Author - Python Programmer                               ############
###		Description - Python Function                            ############
### 	Date - 23-09-2023                                        ############
###																 ############
#############################################################################

import pdb 

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

def builtinfunc():
    #Built-in functions  - given by python itself 
    #Python String Methods
    string1 = "India"
    string2 = "Python Programming"
    
    #Make the string lower case:
    result = string2.casefold()
    print(result)


    #Python String upper() Method
    result = string1.upper()
    print(result)
    
    
    count  = len(string2)
    print("String2 length ",count)
    
    #Python String zfill() Method
    result = string1.zfill(10)
    print(result)
    #https://www.w3schools.com/python/python_ref_string.asp
    
    
    #Python List/Array Methods
    list1 = [10,20,30,40,50]
    list2 = [60,4,55,23,55]
    
    
    fruits = ['apple', 'banana', 'cherry']
    print(fruits)
    fruits.append("orange")
    print(fruits)
    fruits.clear()
    print(fruits)
    count  = len(list1)
    print(count)
    
    #Python List copy() Method
    result = list1.copy()
    print(result)
    
def main() : #All the code written in python are in main function
    # result = printcalc() #calling a function 
    # print(result)
    # result = sum(10,20) #calling a function 
    # print("the sum of two numbers ",result)
    # result = sub(200,20) #calling a function 
    # print("the sub of two numbers ",result)
    # result = multiply(10,10) #calling a function 
    # print("the multiply of two numbers ",result)
    # result = divide(1000,5) #calling a function 
    # print("the divide of two numbers ",result)
    list1 = [10,20,30,40,50]
    numberofelelist(list1) #user define function 
    # #Built in function 
    # builtinfunc()
    print("Using list built in function len",len(list1))
    
    
  
  
if __name__ == "__main__" :
    main()
    

#Assignment 
#1.Write a python user define function which will do following 
# All the trigonometry function calculator(5 enough)
# Find the average of 10 numbers 
# Check for even or odd
# Print fibonacci series 
# Print prime number upto 100 
# Calculate the length of the string and list 

#2.Write a python code to use string built-in function 
# https://www.w3schools.com/python/python_ref_string.asp
# #3..Write a python code to use list built-in function 
# https://www.w3schools.com/python/python_ref_list.asp
# #4..Write a python code to use dictionary built-in function 
# https://www.w3schools.com/python/python_ref_dictionary.asp