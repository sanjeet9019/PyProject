#############################################################################
### 	Author - Python Programmer                               ############
###		Description - Python Operators                           ############
### 	Date - 09-09-2023                                        ############
###																 ############
#############################################################################

#Arithmetic operators

#1.Addition +

number1 = 100
number2 = 200

Sum = number1 + number2

print("Addition =",Sum)

#2.Subtraction - 

number1 = 200
number2 = 100

Subtraction = number1 - number2

print("Subtraction =",Subtraction)

#3.Multiply *

number1 = 10
number2 = 20

Multiply = number1*number2

print("Multiply =",Multiply)

#4.Divison /

number1 = 200
number2 = 10

Divison = number1/number2

print("Divison =",Divison)

#5.Modulus %

number1 = 10
number2 = 3

Modulus = number1 % number2

print("Modulus(remainder) =",Modulus)

#6.Exponent **

number1 = 5
number2 = 4

Exponent = number1 ** number2

print("Exponent =",Exponent)


#Mathematics algebra school times 

# a2 – b2 = (a – b)(a + b)
# (a + b)2 = a2 + 2ab + b2
# a2 + b2 = (a + b)2 – 2ab
# (a – b)2 = a2 – 2ab + b2
# (a + b + c)2 = a2 + b2 + c2 + 2ab + 2bc + 2ca
# (a – b – c)2 = a2 + b2 + c2 – 2ab + 2bc – 2ca
# (a + b)3 = a3 + 3a2b + 3ab2 + b3 ; (a + b)3 = a3 + b3 + 3ab(a + b)
# (a – b)^3 = a3 – 3a2b + 3ab2 – b3 = a3 – b3 – 3ab(a – b)

#1. a2 – b2 = (a – b)(a + b)

a = 5
b = 3 

sqrab =  (a - b) * (a + b)

print("a2 – b2 = ",sqrab)

# 2.(a + b)2 = a2 + 2ab + b2

sqraplusb = (a*a) + (2*a*b) + (b*b)

print("(a + b)2 = ",sqraplusb)

sqraplusb1 = (a**2) + (2*a*b) + (b**2)
print("(a + b)2 = ",sqraplusb1)

# 3.(a + b)3 = (a+b)*(a+b)*(a+b)

cubeandb = (a+b)**3
print(cubeandb)


#Comparison operators

a = 10 
b = 20 
c = 10 

result = (a==b)
result1 = (a==c) 

if result:
    print("a == b")


if result1:
    print("a == c")

print(result)
print(result1)



a = 10 
b = 20 
c = 10 

result = (a!=b) #True 
result1 = (a!=c)  #False 

if result:
    print("a != b")


if result1:
    print("a != c")

print(result)
print(result1)

a = 10 
b = 20 
c = 40 

result = (b>a) #True 
result1 = (a<c)  #True 

if result:
    print("b>a")
    print(result)

if result1:
    print("a<c")
    print(result1)


#Voting age 

govtage = 18 

amit = 25 

result = amit > govtage #True eligible 

if result:
    print("Eligible for voting ",result)
    
if amit > govtage:
    print("Eligible for voting ",result)
    
    
a = 10 
b = 10 
c = 40 

result = (b>=a) #True 
result1 = (a<=c)  #True 

if result:
    print("b>=a")
    print(result)

if result1:
    print("a<=c")
    print(result1)
    
    
num = 100 

num/=20 
#(num = num / 20 )
print(num)


a = 10  #Non zero which is not zero 
b = 20  #Non zero 
c = 0 #zero 
d = 50 
e = -100 

result = (a and b and c)  
result1 = (a and c )

print(result)
print(result1)

# #10 class 
# if ( (math >= 35) and (science >= 35) and (english >= 35) and (hindi >= 35) and (socialscience >= 35))
    # print("This candidate passed ")

#Any non zero value in python programming is always considered as True statement ,for zero as false statement 
if result: #True condition 
    print("(a and b )- Non zero that why true condition")
    
if result1: #False condition -> as it return 0 and 0 considered as false condition in python programming
    print("(a and b )- zero that why False condition")
    
    
a = 10  #Non zero which is not zero 
b = 20  #Non zero 
c = 0 #zero 
d = 50 
e = -100 
d = 0

result = (a or b)  #or as + if(cand1 or cand2 or cand3 .....) -> print(cand3 is the winner)
result1 = (d or c )

print(result)
print(result1)


#Any non zero value in python programming is always considered as True statement ,for zero as false statement 
if result: #True condition 
    print("(a or b )- Non zero that why true condition")
    
if result1: #False condition -> as it return 0 and 0 considered as false condition in python programming
    print("(a or b )- zero that why False condition")
    
    
a = 22  #True -> non zero 
b = 0 #False -> zero 
result = (not a) #False 

print(result)

# #Assignment 
# #1.Write a python program to implement below algebra formulae using arthemetic operators

# # a3 – b3 = (a – b)(a2 + ab + b2)
# # a3 + b3 = (a + b)(a2 – ab + b2)
# # (a + b)4 = a4 + 4a3b + 6a2b2 + 4ab3 + b4
# # (a – b)4 = a4 – 4a3b + 6a2b2 – 4ab3 + b4
# # a4 – b4 = (a – b)(a + b)(a2 + b2)
# # a5 – b5 = (a – b)(a4 + a3b + a2b2 + ab3 + b4)
# #2.Write a python to check a student is pass or fail in class 10 subjects  using python operators and print it 
# ->input number of subject from users using input functions 
# #3.Write a python code to find a use case of "or" operators(with more than 3 or conditions) 
# #4.Write a python code to use of not statement 

#membership operators 

list1 = [10,20,30,40,50]

number = 16 

result =  number not in list1
if result :
    print("In operator",result)

string = "India is my country "
str1 = "is"

tuple = (10,30,40)
number = 30

#Assignment 
#1.Write a python code for implement in/not in operator for string/list/tuple 

10 - 4 * 2

6*2 = 12
10-8 = 2

bitwise & 
1  1   1 
0  0   0
1  0   0
0  1   0