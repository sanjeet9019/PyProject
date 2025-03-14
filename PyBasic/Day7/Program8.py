#############################################################################
### 	Author - Python Programmer                               ############
###		Description - Python Decision making                     ############
### 	Date - 10-09-2023                                        ############
###																 ############
#############################################################################

# #1.if condition 

# age = int(input("Enter your age for checking voting rights "))
# print("Your age is ",age)

# if age>=18: #if this is true 
    # print("If - You are eligible for voting right in India")
    
    
#2.if else condition 

# age = int(input("Enter your age for checking voting rights "))
# print("Your age is ",age)
# a = 10
# b = 20
# if age>=18: #if this condition is true enter if condition
    # print("If-else You are eligible for voting right in India")
    # print("If-else my name is gangadar")
    # c = a+b
    # print(c)
# else : #when if condition is failing then it will come 
    # print("If-else -You are not eligible for voting right in India")
    # c = a+b
    # print(c)
    
#3.if elif else - more than one condition for a variable we need just one condition to passed 

#1.Check for positive 
#2.check for negative 
#3.Check for 0 
#4.
number = 0 

if number>0: #It is a positive number 
    print("Given number is a positive number")
elif number<0:
    print("Given number is a negative number")
else :
    print("Given number is zero ")

priceoftomatoes = 10 

if priceoftomatoes>80 and priceoftomatoes<100: #It is a positive number   # For Australia
    print("price of tomatoes between 80 and 100 in Australia ")
elif priceoftomatoes>=25 and priceoftomatoes<=35:  #Mahastra
    print("price of tomatoes between 25 and 35 in Mahastra ")
elif priceoftomatoes>=10 and priceoftomatoes<=20: #Andhra
    print("price of tomatoes between 10 and 20 in Andhra ")
else :
    print("Else condition  ")
    
    
#Nested if condition 

vehicle = "Car"
tyres = 4 
if vehicle == "Car":
    if tyres == 4 :
        print("Yes this is a car and it has 4 tyres")
else :
    print("It is a not car " )
    

age = 20 
nationaly = "Indian"

if age >= 18 :
    if nationaly == "Indian" :
        print("You are eligible for voting ")
        
        
number = 10 

if number > 10:
    if number > 50 :
        if number > 100:
            print("Number is greater 100")
            
            
#Assignment 
#1.Write a python code for implement in/not in operator for string/list/tuple
#2.Write a python code to check for a person for grade using elif condition
# 1st class  = 60 > and <100
# 2nd class  = 40 > and <59
# 3rd class  = 35 > and <39
#3.Write a python code to check for a number is Prime or not ? 
#4.Write a python code to check for a number is even or not ? 
#5.Write a python code to use nested if condition (you can find a use case for that )