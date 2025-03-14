#############################################################################
### 	Author - Python Programmer                               ############
###		Description - Python Loops                               ############
### 	Date - 16-09-2023                                        ############
###																 ############
#############################################################################

import pdb

def main() :
    #print 1-10 numbers 
    # num1 = 1
    # print(num1)
    # num2 = 2 
    # print(num2)
    # num3 = 3
    # print(num3)
    # num4 = 4
    # print(num4)
    # num5 = 5
    # print(num5)
    # num6 = 6
    # print(num6)
    # num7 = 7
    # print(num7)
    # num8 = 8
    # print(num8)
    # num9 = 9
    # print(num9)
    # num10 = 10
    # print(num10)
    
    #print 1-10 numbers using while loops 
    num = 1 
    # pdb.set_trace()
    while (num<=10) :
        print(num)
        num = num + 1 


    #print even numbers from 1 to  100 using while loops  (2,4,6,....100)
    num = 2 
    while (num<=100) :
        print(num)
        num = num + 2
        
        
    #print even numbers from 1 to  100 using while loops  (2,4,6,....100)
    num = 1 
    while (num<=100) :
        if ( num % 2 == 0) :
            print("Even number using %",num)
        num = num + 1

    #print odd numbers from 1 to  100 using while loops  (2,4,6,....100)
    num = 1 
    while (num<=100) :
        print(num)
        num = num + 2
        
        
    #print multiplication of 5 
    num = 1 
    multiplication = 10 
    while (num<=10) :
        result = multiplication * num 
        print(multiplication,"*",num,"=",result)
        num = num + 1
        if num == 5 :
            break  # to break the while loop condition 


if __name__ == "__main__" :
    main()
    
    
    
#Assignment 

#Assignment 
#1.Write a program to find a crash/wrong code for 
# a = 100 int, b = "10" string 
# a)int+string,int/string,int/string- adding/multiply ,float / string operation 
# b)multiple by 0 , divide by 0 
# c)algebra formula(a+b)^2 
#2.Write a python code using while loop printing square and cube of a number(input) upto 10 
#3.Write a python code using while loop to print all prime number upto a given input (10)
# 10 -> 2,3,5,7
# 20 -> 2,3,5,7,11,13,17,19 

# num = 1 
# while (num < = 10)
    # if(num %2 == 0 )
        # print(num) 
    # num = num + 2 
#4.Write a python code using while loop to print 10 employee details 
# emp details : 
# name 
# employe num 
# location 
#5. Write a python code to do sum of the number (1+2+3,4,5,6,7,8,9,10) 
#6.Write a python code to print fibonacci series for a given number  1,1,2,3,5,8,13..... 
# #7.Write a python code to add the content of a list 

# list1 = [10,20,30,40,50]

# num = 0 
# sum = 0 
# while ( num <=5)
    # sum = sum + list1[num]

# a = [1,2,3]
# a = [[10,20,30],[30,40,50]]

# b= a[0] = [10,20,30]


#For loop 

# for counter in sequence(list,tuple,string) :

list1 = [10,20,30,40,50]
string = "India is my country "

for count in list1:
    print("For loop list ",count)
    
    
for alpha in string:
    print("For loop string",alpha)

    
    
#range(start,stop,increment)

list2 = list(range(1,11,1))
print(list2)

multipy = 3
for num in range(1,11,1):
    result = multipy * num
    print(multipy,"*",num,"=",result)
    

# while True : #infinite loop conditions means program never ever ends 
    # name = input("Enter your name")
    # if ( name == "No"): # always have some break condition you can come out from the loop 
        # break
    # print(name)
    

print("Nested for loop ")
for outer in range(1,11,1): #row 
    for inner in range(1,11,1): #column 
        result = outer * inner 
        print(outer,"*",inner,"=",result)
        
print("Nested while loop ")
outer = 1 
while (outer<=10):
    inner = 1 
    while(inner<=10):
        result = outer * inner 
        print(outer,"*",inner,"=",result)  
        inner = inner + 1 
    
    outer = outer + 1 
    if(outer == 6):
        break
        
        
#print 1-10 numbers using while loops 
num = 1 
while (num<=10) :
    if (num == 5) :
        num = num + 1
        continue  
    print(num)
    num = num + 1 
    

    
# #Assignment :
# 1.Write a python code for loop to add a number from 1 to 100 
# 2.Write a python code for loop to print even and odd numbers 
# 3.Write a python code using nested for loop for print state and their list of vegetables present 
# 4.Write a python code using nest loop for doing calculation student and their average marks using list(inside dictionary)

# list = [ {name : amit ,score : [30,506,60,60},  or using input function to create the list 
         # {name : sree ,score : [30,506,60,60},
         # {name : madhu ,score : [40,506,60,60}]
         
# 5.Write a python code using infinite while loop to get caculation of algebra formula 

# while True :
    # 1 = a2 – b2 = (a – b)(a + b)
    # 2 (a + b)2 = a2 + 2ab + b2
    # 3  a2 + b2 = (a + b)2 – 2ab
    # 4 (a – b)2 = a2 – 2ab + b2
    # if ( choice == "No")
        # break :
# optional :
# Write a python code using infinite while loop to live current hdd space in your laptop 
# 6.Write a python code to using continue keyword to print 1 to 10 (except 5) 
