#############################################################################
### 	Author - Python Programmer                               ############
###		Description - Python Data types                          ############
### 	Date - 03-09-2023                                        ############
###																 ############
#############################################################################

#Dictionary data types 

#1st way to define a dictionary (employee name --> employee number ,mapping can be anything  
#string -> string 
#int -> int 
#float -> int 
#int -> float (convert a int to a float 100 -> float(100) , ......)
#int -> list (Make a dictionary of prime number (5 -> [1,5] ,10 -> [1,2,3,5,7] upto 30)
#int -> tuple 
#string -> list 

dict1 = {"sree":1000 ,"venkat":1022,"ashish":1022,"amit":1033}  

print(dict1) #print whole dictionary
print(dict1["sree"]) #print corresponding values 

dict1["sree"] = 2000 #update the values using keys 

print(dict1["sree"])

#+ ,*,/ is not applicable for dictionary

#2nd way to define a dictionary

dict2 = {} 

#Squaring of a number  2^2 = 4 , int -> int mapping , number -> square of a given number 
dict2[1] = 1 
dict2[2] = 4
dict2[3] = 9
dict2[4] = 16
dict2[5] = 25
dict2[6] = 36
dict2[7] = 49
dict2[8] = 64
dict2[9] = 81
dict2[10] = 100

print(dict2)
print(dict2[3]) #key to get values 

dict2[3] = 90

print(dict2[3]) #key to get values 
print(dict2.keys())
print(dict2.values())

#Numorology -> subcarrier spacing  ( 2^numorlogy * 15)
dict3 = {}

dict3[0] = 15 
dict3[1] = 30
dict3[2] = 60
dict3[3] = 120
dict3[4] = 240


#Assignment 
#1.Create a dictionary of  cube of a number upto 10 and print it (int to int mapping ) 1->1,2->8,3->27,4->64,5->125
#2.Create a dictionary with employee name as key and add his mobile number ,location and email id using list (string -> list mapping) 
#3.Create a dictionary with a given number and corresponding all the prime number (int -> list mapping) (upto 1-10 prime number ) 
#4.Create a sample dictionary with first and second method above (prefer second method to define a dictionary)

boolT = True 
boolF = False 
value = None 

print(boolT)

if boolT :
    print("boolT is true ")
    
# #5.Write a python code using True,False and None data types to use in your if condition to check a even number 
# -> if even number -> True 
   # else > False 
   # else -> None 