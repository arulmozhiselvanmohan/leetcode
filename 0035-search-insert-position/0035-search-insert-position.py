class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        my_ref = set(nums)
        
        if target in my_ref:
            return nums.index(target)
        else:
            for i in range(1,len(nums)+1):
                if target-i in my_ref:
                    return nums.index(target-i)+1
                elif target+i in my_ref:
                    return nums.index(target+i)
            return 0       
            
            

        
      

                   

    