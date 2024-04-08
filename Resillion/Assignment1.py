#############################################################################
###     Author - Sanjeet Prasad                                  ############
###     Description - Resilision Python Assignment               ############
###     Date - 09-12-2023                                        ############
###                                                              ############
#############################################################################

#import regular expression 
import re

def longest_ascending_digit_sequence(input_string):
    '''
    input
    -----
    Provide the input_string
  
    Notes
    -----
    Takes the input string and returns the longest sequence of ascending order of numbers inside 
    the string
  '''
    #Using regex to find only the digit as list from the given string 
    digit_sequences = re.findall(r'\d+', input_string)
    
    #Calculate the longest ascending integer numbers in a given list of numbers 
    max_sequence_length = 0
    for sequence in digit_sequences:
        current_sequence_length = 1
        for i in range(1, len(sequence)):
            if int(sequence[i]) == int(sequence[i - 1]) + 1:
                current_sequence_length += 1
            else:
                break
        max_sequence_length = max(max_sequence_length, current_sequence_length)
    
    return max_sequence_length

def main():
    # Test cases 
    # text_input = "12345ab456cd789ef12"
    # text_input = "23ab456cd789ef12"
    # text_input = "14ab45689cd789ef12"
    # text_input = "0ab0456cd789ef12"
    text_input = "ab4506cd70890ef1234904"
    result = longest_ascending_digit_sequence(text_input)
    print(result)

if __name__ == "__main__" :
	main()
