class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        length = len(digits)

        for i,value in enumerate(digits):
            number += (digits[i]) * (10 ** (length-i-1))
        
        number +=1 

        digit_list = [int(digit) for digit in str(number)]       

        return digit_list


    
            