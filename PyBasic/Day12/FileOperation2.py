#############################################################################
### 	Author - Python Programmer                               ############
###		Description - Python File Operation                      ############
### 	Date - 07-10-2023                                        ############
###																 ############
#############################################################################

#Input from keyboard 
#Input functions 

#Output to screen 
#print function 

#File operation in Python programmin language 
#1.Open the file 
#2.Read/write/delete/search 
#3.Close the file 
from datetime import date

def main():

    #read() tell() and seek()  
    filename = r"otherfile.txt"
    with open(filename,"r") as fileptr : #1.Open the file r - raw absolute path 
        filepos = fileptr.tell()
        print("File position just after open the file ",filepos)
        readcontent = fileptr.read() #2 Read the file 
        filepos = fileptr.tell()
        print("File position just after read()",filepos)
        print("open read \n",readcontent)
        fileptr.seek(0,0)
        filepos = fileptr.tell()
        print("File position just after seek(0,0)",filepos)
        readcontent1 = fileptr.read() #2 Read the file 
        print("open read1 \n",readcontent1)
        filepos = fileptr.tell()
        print("File position now",filepos)
        
        fileptr.seek(0,1) #end of the file 
        filepos = fileptr.tell()
        print("File position now",filepos)
        readcontent2 = fileptr.read() #2 Read the file 
        print("open read2 \n",readcontent2)
        
       
        seek(0,0) 
        helping you to move file position
        second argument 0 -> take you to the begining of the file ,1-> current file ptr ,2 -> take you at the end of file 
    today = date.today()
    name = "rahul"
    string = f"hello world my name is {name}"
        #write -> if no file is there ,create automatically and write from the begining ,if file exist ,it will overrides it 
    with open(r"PassTestCase.txt","w") as fileptr : #1.Open the file r - raw absolute path 
        #5G Throughput test is passed 
        print("File created for writing ")
        fileptr.write(f"Test case number 1 - 5G Throughput test is passed {today} \n")
        fileptr.write(f"Test case number 2 - NR Handover is passed {today}\n")
        fileptr.write(f"Test case number 3 - LTE to NR reselection is passed {today} \n")
        
    with open(r"FailTestCase.txt","w") as fileptr : #1.Open the file r - raw absolute path 
        #5G Throughput test is passed 
        print("File created for writing ")
        fileptr.write("Test case number 1 - 4G Throughput test is fails  \n")
        fileptr.write("Test case number 2 - LTE Handover is fail \n")
        fileptr.write("Test case number 3 - NR to LTE reselection is fail \n")

    with open(r"testw.txt","w") as fileptr : #1.Open the file r - raw absolute path 
        pos = fileptr.tell()
        print("Current position now ",pos)
        print("File created for writing ")
        fileptr.write("Test case number 1 \n")
        fileptr.write("Test case number 2 \n")
        fileptr.write("Test case number 3\n")


    with open(r"testw.txt","a") as fileptr : #1.Open the file r - raw absolute path 
        pos = fileptr.tell()
        print("Current position now ",pos)
        print("File created for append ")
        fileptr.write("Test case number 4 \n")
        fileptr.write("Test case number 5 \n")
        fileptr.write("Test case number 6\n")


    with open(r"testw.txt","r+") as fileptr : #read the file first you can then you can write 
        pos = fileptr.tell()
        print("Current position now ",pos)
        content = fileptr.read()
        pos = fileptr.tell()
        print("Current position1 now ",pos)
        print("r+ content ",content)
        fileptr.write("We got the msg ")
        
     #w+ -> first write the file ,read the files 
     #a+ -> open the file for append then it can used read A
    
if __name__ == "__main__" :
    main()
    
    
#Assignment 
# #1. Write a python code to  do following things 
# - Write the algebra formulae in a text file called algebra.txt 
# - Write the Student information like name,age,class in a text file called student
# - Read these above two files using w+/r+ 
# 2.Write a sample code for use of a+ mode python 
# 3.Write a code to use of seek() functions and tell functions while reading same file twice and write twice as well 
# test.txt 
# >read the file twice 
# ->write the file twice 
