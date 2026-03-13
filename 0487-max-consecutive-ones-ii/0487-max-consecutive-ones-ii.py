class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l,r=0,0
        num_of_zeros=0
        length_of_sequence=0

        while r < len(nums):
            if nums[r] == 0:
                num_of_zeros +=1
            
            while num_of_zeros ==2:
                if nums[l]==0:
                    num_of_zeros -=1
                l+=1
            
            length_of_sequence = max(length_of_sequence, r-l+1)
            r+=1
    
        return length_of_sequence
        
        