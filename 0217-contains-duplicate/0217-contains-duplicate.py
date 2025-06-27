class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        nums.sort()
          
        
        for j in range(1,len(nums)):
            if(nums[j-1]==nums[j]):
                return True
                break
        
        return False

       