#############################################################################
### 	Author - Python Programmer                               ############
###		Description - Python Regular expression                  ############
### 	Date - 15-10-2023                                        ############
###																 ############
#############################################################################

import module 

def classexample():
    Person1 = module.Person("Amit",25,"male")  #proper noun - objet1 
    Person2 = module.Person("Sree",30,"male")  #proper noun - objet2 
    Person3 = module.Person("Hema",16,"female")  #proper noun - objet3 
    Person1.persondetails()
    Person2.persondetails()
    Person3.persondetails()
    Person3.sleeping()
    Person1.sleeping()
    Person2.sleeping()
    result = module.add(10,20)
    print("Sum of two number",result)

    math1 = module.Math(200,100)   #proper noun - objet1 for math1 
    math1.add()
    math1.sub()
    result1 = math1.mul(10,10,10)
    print("Multiplication of two numbers" ,result1)
    result2 = math1.divide()
    print("Division of two numbers" ,result2)
    result3 = math1.mul(10,20,30)
    print("Multiplication of two numbers" ,result3)
    
def main():
 
    classexample()
    
if __name__ == "__main__" :
    main()
    
