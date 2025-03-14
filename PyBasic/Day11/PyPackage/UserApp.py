#############################################################################
### 	Author - Python Programmer                               ############
###		Description - Python User application                    ############
### 	Date - 24-09-2023                                        ############
###																 ############
#############################################################################
import Math   #User define  module 
import String #User define  module 
import pandas #Built in/standard module 
import pdfreader


def main():

    #Used the math module 
    result = Math.sum(10,30)
    print("Sum = ",result)
    
    result = Math.sub(40,30)
    print("Subtraction = ",result)
    
    result = Math.sqroftwo(10,10)
    print("sqroftwo = ",result)


    #Used the string module 
    result = String.stringlen("India")
    print("Strlen = ",result)
    
    String.printstring("India is my country")



#main program 
#User program
#user define program
#User application
if __name__ == "__main__" :
    main()
    
    
#https://pdfreader.readthedocs.io/en/latest/tutorial.html

# #Steps to call a user program from different path 

# #1.Create a set up file ,give name ,version details 
# from setuptools import setup,find_packages

# setup(name = "PyPackage30thSep",
      # version = "1.0",
      # packages = find_packages()
      # )
# #2.pip install . 
# it will club all the present modules/folders into a single package given on  name section of setup 
# #3.Then you can call your user program from anywhere in your pc 
#4. uninstall package pip list -> pip uninstall packagename 


#Assignment 
# #1.Write your python packages which do following things 
# Maths folder
# --->integration.py 
# --->Algebra.py 

# 1.All the math integration function (2 operations) integration.py 
# https://docs.scipy.org/doc/scipy/tutorial/integrate.html
# 2Algebra module - 3 functions(Algebra.py )

# DataTypes folder 
# --->ListOperation.py ( 2 operations)
# --->Dictionary.py ( 2 operations)
# --->string.py ( 2 operations)

# UserProg.py to use this functions
# Setup.py 

# #2.Create your own python package for doing xml parsing(use in built package inside it )
# https://www.edureka.co/blog/python-xml-parser-tutorial/
#https://pdfreader.readthedocs.io/en/latest/tutorial.html - Optional 