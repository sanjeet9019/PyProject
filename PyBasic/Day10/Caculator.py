#############################################################################
### 	Author - Python Programmer                               ############
###		Description - Python Module example                      ############
### 	Date - 24-09-2023                                        ############
###																 ############
#############################################################################

import module as calc
import math 
import matplotlib.pyplot as plt
import pandas
import xml.etree.ElementTree as ET

def main():
    
    #Sum of two numbers 
    result = calc.sum(10,20)
    print("Sum of two numbes ",result)
    
    #Sub of two numbers 
    result = calc.sub(100,20)
    print("Sub of two numbes ",result)
    
    #Multiply of two numbers 
    result = calc.multiply(10,10)
    print("multiply of two numbes ",result)

    #PI value 
    print("PI value  ",calc.PI)
    
    
    #Using math module 
    result = math.pow(2, 3) 
    print("Using math module  pow(2, 3) ",result)

    result = math.sqrt(16) 
    print("Using math module  math.sqrt(x) ",result)
    
    #Using matplotlib modules 
    print("matplotlib modules to generate graph")
    # x axis values
    x = [1,2,3]
    # corresponding y axis values
    y = [2,4,1]
  
    # plotting the points 
    plt.plot(x, y)
  
    # naming the x axis
    plt.xlabel('X = axis')
    # naming the y axis
    plt.ylabel('Y = axis')
  
    # giving a title to my graph
    plt.title('Graph generate')
  
    # # function to show the plot
    # plt.show()

    #Pandas module 
    #dictionary 
    mydataset = {
                    'cars': ["BMW", "Volvo", "Ford"],
                    'passings': [3, 7, 2]
                }
    myvar = pandas.DataFrame(mydataset)
    print(myvar)
    
    #XML Parse module 
    mytree = ET.parse('sample.xml')
    myroot = mytree.getroot()
    print(myroot)
    print(myroot.tag)
    print(myroot.attrib)
    print(myroot[0].tag)
    for x in myroot[0]:
     print(x.tag, x.attrib)
    for x in myroot[0]:
        print(x.text)


    

if __name__ == "__main__" :
    main()
    
    
#Assignment 
#1.Write your own module for string operation (strlen ,str cancation ,string compare,string search)
# string.py
# userapp.py
#using your module to develop your application 
#2.Write your own module for banking software maintaining a accounts 
# Account number 
# Account name 
# Balance 
# use this module in your application to see how many accounts are their along with name and balance 
# AddAccountnumber
# Accountname 
# Balance
# banking.py module name 
# userapp.py 
#3.Write a python code to use math module in your program with atleast 20 functions from each category 
#4.Write a python to use all the function from matplotlib.pyplot   -5 functions 
# https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
# https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html
#5.Write a python code to use pandas library  and use for excel sheet operatios (read a csv file,update a csv file ) -5 functions 
#6.Write a python code to use xml paring module  and use for decode each message inside the xml  -5 functions 
# https://www.edureka.co/blog/python-xml-parser-tutorial/