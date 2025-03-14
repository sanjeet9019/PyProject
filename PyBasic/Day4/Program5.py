#############################################################################
### 	Author - Python Programmer                               ############
###		Description - Variables                                  ############
### 	Date - 02-09-2023                                        ############
###																 ############
#############################################################################

#variables 

number = 100 #as you define a variable ,memory is allocated by python itself 4 bytes is allocated for number 
number2 = 200 

name = "Python" 

print(number)

del number

a = b = c = d = 100 #mutiple assignent to the same values 

#variable name 

 #start with letter and __ sign 
string = "India"  #valid 
_string = "India" #valid 
# 5string = "India"  #Invalid 
num = 100 #valid 
NUM = 200 #valid 
# if = 300 keyword cannot be used as variable name Invalid 

#variable name always start with a letter(a,A) and _ sign 
#cannot use number or special charater to start a variable name 
#cannot use the keyword to define a variable 

number123 = 500 

#Assignment 
#1.Write a python program where define 10 valid variable names and 10 invalid variable name 

#Python Data types 

#Numeric datatypes 

#1.Integer 

num1 = 100 
num2 = 200
num2 = -100 

#2.Float 

float1 = 100.00
pi = 3.14 

print(num1,float1)
print(pi)

#3.String 

string1 = "Python"
string2 = "Programmer"
string4 = "100"

print(string1) 
print(string1[0]) #Index start from 0 and onwards 

string = string1 + string2 #concentation ->addition 
string3 = 2*string
string5 = 2*string4

print(string)
print(string3)
print(string5) 

#string operation 
#1.Index get each letter 
#2. Add two string
#3.print whole string
#4.Multiply string n number of times 

#typecast in python 

#1.integer to a float 

intnum = 150 
print(intnum)

floatnum = float(intnum)
print(floatnum)

#2.string to int 

string = "100" 
string1 = 2*string 
print(string1) 

intstr = int(string) 
intmul = 2*intstr 
print(intmul)


# age = input("Enter your age ") #always return string -> "100"
age = 100
intage = int(age) 
print(intage)

print(type(intage),type(string))

#Assignment 
#2.write a python code to define datatypes of 5 int,5 float values and 5 string values 
#3.Write a python code to do string operation (addition ,mutiplication ,index 3 )
#4.Write a python code to do typecast from int to float ,float to int ,string to int ,int to string etc 

#List Data types 
#store employee details ,student details 

list1 = [10,20,30,40,50,60]
list2 = [70,80,90,100,110]
list5 = ["Gangadhar","Hema","venkat"]
list3 = list1 + list2 
list4 = 2*list1
list5[0] = "Ashish"  #Update the value of list using index option ,list index start from 0 
# list5[3] = "Gangadhar" assignent 

print(list1)
print(list1[0])
print(list3)
print(list4)
print(list5)

list6 = []  #empty list 

print(list6)

#Assignment
#5.Write a python code to do all list operation (print whole list ,add list ,multiply list and update the value of list ) 
#6.Write a python code to add a new element in a given list without using any function 
#7.Write a python code to add each element of a given list (assume list contains 10,20,30,40,50)


#Tuple sequence datatypes in python 

tuple1 = (10,20,30,40,50,60) #read only values no one can changed 
tuple2 = (70,80,90,100,110)
print(tuple1)
print(tuple1[3])

tuple3 = tuple1 + tuple2
print(tuple3)

tuple4 = 2*tuple1
print(tuple4)

# tuple1[0] = 100 #this is not supported 

#Assignment
#6.Write a python code to do all tuple operation (print whole list ,add list ,multiply list and update the value of list ) 
#7.Write a python code to add a new element in a given tuple without using any function 
#8.Write a python code to add each element of a given tuple (assume list contains 10,20,30,40,50,60)

