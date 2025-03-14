#############################################################################
### 	Author - Python Programmer                               ############
###		Description - Python Regular expression                  ############
### 	Date - 14-10-2023                                        ############
###																 ############
#############################################################################
import re 

def regex():
    text = r"India is my country ,I love my country . we are doing python class \
           today we have amit ,ashish ,hema ,venkat ,madhu in the class . \
           Amit mobile is +91 995821763 ,ashish number +44 123234445, hema number is +1 342345556,madhu +92-56754556 \
           and amit has email id as amit.python@gmail.com ,venkat has email id as venkat_python12@gmail.com \
           Hema has email id as hema_python12@yahoo.co.uk \
           amit salary is $1200, hema salary is $1400.55 ,venkat salary is $5500.453 "
           
    string = "email id as"
    pattern1 = rf"{string}"            
    pattern2 = r"\+\d+\D?\s?\d+"         #mobile number   
    pattern3 = r"\w+\.?\w+\@\w+\.\w+\.?\w+"   #emaild  hema_python12@yahoo.co.uk
    pattern4 = r"\$\d+\.?\d+"  #salary 
    pattern5 = rf"{string} \$\d+\.?\d+"  #salary 
    pattern5 = rf"{string} {pattern3}"  #salary 
    list1 = re.findall(pattern5,text)
    print("This is from simple text ")
    for data in list1 :
        print(data)
        
    filepath = r"text.txt"
    try :
        with open(filepath,"r") as fileptr :
            content = fileptr.read()
            list1 = re.findall(pattern2,content)
            print("This is from file ptr")
            for data in list1 :
                print(data)
    except FileNotFoundError:
            print("FileNotFoundError exception has arrived ")


    #re.search(pattern,text)
    match = re.search(pattern1,text)
    print(match.group())
    
    #re.split(pattern,text))
    text2 = r"amit salary is $1200, hema salary is $1400.55 ,venkat salary is $5500.453"
    pattern = r"\s"
    list2 = re.split(pattern,text2)
    print(list2)
    for data in list2 :
        print(data)
        
    #re.sub(pattern, replace,text,max)
    pattern7 = r"\$\d+\.?\d+"  #salary 
    replace = r"****"
    updatedstring = re.sub(pattern7, replace,text2)
    print(updatedstring)

           
    
def main():
 
    regex()
    
if __name__ == "__main__" :
    main()
    

#Assignment 
#Write a python code to use regex to findall 5 diffrent email id ,5 diffrent types of mobile numbers 
#write a python to demonstate real time use of sub ,search split 