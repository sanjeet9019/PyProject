#############################################################################
### 	Author - Python Programmer                               ############
###		Description - Python Sample example code                 ############
### 	Date - 26-08-2023                                        ############
###																 ############
#############################################################################

#define two numbers 

num1 = 100
num2 = 200

# num2 =  called syntax error become you have not define anything ,program will not execute at all you must have to define something to fixed 

#define two name

name1 = "Ankur"
name2 = "Hemlatha"

print(num1)
print(num2)

# print(num2 sytax error -> right braces is missing 

# num3 = num2/0 -> this is called run time error and program will stop in this point after executing all above statement and will not execute below
num3 = num2/10 #then run time fixed by divide by a valid number 

print(name1)
print(name2)

string = input("Enter something ") 
print(string)

# print(string1) this is run time error as we dont have define it 
#print and input are the library function 

#Assignment 
#1.Write a python program where you can generate upto 5 unique syntax error 
#2.Write a python program where you can generate upto 5 unique run time  error 
#3.Write a python program where you can take the input(name,age and gender) from user/keyboard and print in the screen 


#del reserved keyword examples 
del string
print(string)

del num1 
print(num1) 