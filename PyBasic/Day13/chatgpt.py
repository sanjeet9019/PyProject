#############################################################################
### 	Author - Python Programmer                               ############
###		Description - Python ChatGpt,OS ,try and exception       ############
### 	Date - 08-10-2023                                        ############
###																 ############
#############################################################################

import json
import xml.etree.ElementTree as ET
import os 

#print even number 
def printevennumber():
    #Print even number from 1-100 
    for number in range(1, 101):
        if number % 2 == 0:
            print(number)


def readjsonfile():
    # Specify the path to your JSON file
    json_file_path = "sample1.json"  #r"c/path/sample1.json"
    try :
        # Open and read the JSON file
        with open(json_file_path, "r") as json_file:
            # Parse the JSON data
            data = json.load(json_file)
    except FileNotFoundError:
        print("FileNotFoundError exception has arrived ")
    else :
        print("File is present ")

    # Access the data as a Python dictionary
    print("Name:", data["name"])
    print("Age:", data["age"])
    print("City:", data["city"])


def xmlparsing():

    # Specify the path to your XML file
    xml_file_path = "samplexml.xml"
    # Parse the XML file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Access and print elements and their values
    for item in root.findall('item'):
        name = item.find('name').text
        price = item.find('price').text
        print("Name:", name)
        print("Price:", price)

def filehandling():
    current_filename = r"sample2.json"
    new_filename = r"sample2.json"
    # os.rename(current_filename, new_filename)
    # os.remove(new_filename)
    # print(f"{new_filename} is deleted")
    foldername = r"PythonCode"
    # os.mkdir(foldername)
    # print(f"{foldername}folder is created")
    os.rmdir(foldername)
    print(f"{foldername}folder is deleted")
    
#https://docs.python.org/3/library/exceptions.html
def tryandexception():
    try :
        with open("abc.txt","r") as file :
            content = file.read()
            print(content)
    except ZeroDivisionError:
        print("ZeroDivisionError exception has arrived ")
    except FileNotFoundError:
        print("FileNotFoundError exception has arrived ")
    else :
        print("Code is Ok ")
  
    try :
        a = 10 
        b = 0 
        divide = a/b 
        multiply = a * b 
        print(divide) #exception 
        print(multiply)
    except ZeroDivisionError:
        print("ZeroDivisionError exception has arrived ")
    else :
        print("Code is Ok ")
        
    print("end of try and exception ")
    
    
def main():

    # #print even number 
    # printevennumber()
    
    # #read json  file  
    readjsonfile()

    # #parse xml file  
    # xmlparsing()
    
    # #OS file 
    # filehandling()
    
    #tryandexception
    # tryandexception()


if __name__ == "__main__" :
    main()
    

#Assignment 
# 1.Read a sample pdf file and print using chat gpt 
# 2.Read a html file and print the content using chat gpt 
# 3.Write a python code using chatpt to read a file and put the content into a excel sheet 
#4.Write a code using chatpt to use pandas library to create a report of 10 employee with their employee id,salary and department
#5 write a python to use of OS package to implement 10 file handling functions 
#6.Write a python code to handle try and exception for 5 real time scenario 
# -> divide by 0 
# -> file is not found 