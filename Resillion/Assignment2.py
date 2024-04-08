#############################################################################
###     Author - Sanjeet Prasad                                  ############
###     Description - Resilision Python Assignment               ############
###     Date - 09-12-2023                                        ############
###                                                              ############
#############################################################################

''' Problem statement 
In Python, or the programming language of your choice, write a function that takes as its two inputs i) a list/array of unsorted numbers and ii) a target number. 
A ‘triplet’ is a set or list of three numbers in the array, which do not need to be consecutive (next to one another in the array). Your function should find the 
triplet in the array whose sum is as close to the target number as possible and return the sum of the triplet (the result of adding the three elements of the triplet
 together). If there is more than one such triplet, return the sum of a/the triplet with the smallest sum.  '''

def closest_triplet_sum(nums, target):
    '''
    input
    -----
    number of integers list and target number 
  
    ouput 
    -----
    Sum of close triplet 
    
    Notes
    -----
    Takes the input numbers list and returns the sum of closest triplet 
    '''
    #first sort the numbers 
    nums.sort()
    closest_sum = 0 

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum

            if current_sum < target:
                left += 1
            else:
                right -= 1

    return closest_sum


def main():
   # Test cases :
   numbers_list = [1, 2, -1, 4, 5]
   target_number = 6
   result = closest_triplet_sum(numbers_list, target_number)
   print(result)

if __name__ == "__main__" :
    main()
