#############################################################################
### 	Author - Python Programmer                               ############
###		Description - Python File Operation                      ############
### 	Date - 01-10-2023                                        ############
###																 ############
#############################################################################
import math 

#Input from keyboard 
#Input functions 

#Output to screen 
#print function 

#File operation in Python programmin language 
#1.Open the file 
#2.Read/write/delete/search 
#3.Close the file 


def main():
    # name = input("What is your name ") #input from keyboard
    # age = input("What is your age ")
    # print("My name is ",name,"age is ",age)
    
    #1st way of reading 
    fileptr = open(r"C:\Users\x\Desktop\Python\batch12\Day12\FileOperation.py","r")  #1.Open the file r - raw absolute path 
    readcontent = fileptr.read() #2 Read the file 
    print("open read \n",readcontent)
    fileptr.close()
    
    #1.Always open file with r - raw 
    #2.Always give full path in open 
    #3.read() function to read whole file content ,read(number) give some bytes 
    
    #2nd way of file open 
    with open(r"C:\Users\x\Desktop\Python\batch12\Day12\PyPython.txt","r") as fileptr: 
        for eachline in fileptr :
            print(eachline.strip())
            
            
    #3rd way read a file 
    with open(r"C:\Users\x\Desktop\Python\batch12\Day12\PyPython.txt","r") as fileptr: 
        while True:
            content = fileptr.readline()
            print("readline()",content.strip())
            if not content : 
                break 



    #read() tell() and seek()  
    fileptr = open(r"C:\Users\x\Desktop\Python\batch12\Day12\FileOperation.py","r")  #1.Open the file r - raw absolute path 
    readcontent = fileptr.read() #2 Read the file 
    print("open read \n",readcontent)
    fileptr.close()
    








if __name__ == "__main__" :
    main()
    
    

#Assignment 
# #1.Write a python code do following operation 
# - open 
# - with open 
# - read()
# - each line 
# - read some bytes 
#input file for read/open - FileOperation.py 