################################################################################
###                             					        ####################
### Author - Rahul                					        ####################
### Description - Python Algebra                            ####################
### Math calculator module      						    ###################
###                                 						####################
### Date - 9th July 23          							####################
################################################################################
# Basic Algebra Formula
# a2 – b2 = (a – b)(a + b)
# (a+b)2 = a2 + 2ab + b2
# a2 + b2 = (a – b)2 + 2ab
# (a – b)2 = a2 – 2ab + b2
# (a + b + c)2 = a2 + b2 + c2 + 2ab + 2ac + 2bc
# (a – b – c)2 = a2 + b2 + c2 – 2ab – 2ac + 2bc
# (a + b)3 = a3 + 3a2b + 3ab2 + b3
# (a – b)3 = a3 – 3a2b + 3ab2 – b3

# a2 – b2 = (a – b)(a + b)
def square_of_twonumber(a, b):
    result = (a - b) *(a + b)
    return result 

    
# (a + b)2
def square_of_sum(a, b):
    result = (a - b) *(a - b) 
    return result
    
# (a – b)2
def square_of_difference(a, b):
    result = (a - b) ** 2
    return result 
