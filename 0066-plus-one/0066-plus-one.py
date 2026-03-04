class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        length = len(digits)

        for i,value in enumerate(digits):
            number += (digits[i]) * (10 ** (length-i-1))
        
        number +=1 

        digit_list = []

        for digit in str(number):
            digit_list.append(int(digit))     

        return digit_list


    
            