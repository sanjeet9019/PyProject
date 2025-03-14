#############################################################################
### 	Author - Python Programmer                               ############
###		Description - Python Debugger                            ############
### 	Date - 16-09-2023                                        ############
###																 ############
#############################################################################

#write this line 
import pdb 
import module as calc
#we must use use if statement main 
#def main 
#it helps to tell that this is the main file /starting python file for a project(have more than 1 files)
def main():
    
    a = 10 
    pdb.set_trace()  #This is the line you have to add -> breakpoints 1
    print(a)
    if (a > 5):
        print("a > 5")

    num1 = 100
    num2 = 10 
    pdb.set_trace() #break point 2 
    divide = num1/num2 
    print("Divide two numbers ",divide)

    #Sum of two numbers 
    result = calc.sum(10,20)
    print("Sum of two numbes ",result)


    a = 40
    b = 10
    c = 20    
    pdb.set_trace() #break points 3 
    if (a>b):
        if(a>c):
            print("a is a largest number")

if __name__ == "__main__" :
    main()
    
    
#Python debugger steps 
#1. import pdb 
#2. add pdb.set_trace() where you think the code got wrong ????
#3.Then use the python debug command while program is executing n ,c,s,l,q,p
#4.After found the issue in the code and fixed it in the code 
#5.Delete all the break points ( pdb.set_trace())


#Assignment 
#1.Write a program to find a crash/wrong code for 
# a = 100 int, b = "10" string 
# a)int+string,int/string,int/string- adding/multiply ,float / string operation 
# b)multiple by 0 , divide by 0 
# c)algebra formula(a+b)^2 