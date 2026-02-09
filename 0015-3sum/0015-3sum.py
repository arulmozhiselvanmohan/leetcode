class Solution:
   
   def threeSum(self, nums: List[int]) -> List[List[int]]:
    target = 0
    result = []
    nums.sort()  # Ensure the array is sorted for the two-pointer technique

    for i in range(len(nums)):
        # Skip duplicate values for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        j, k = i + 1, len(nums) - 1
        target = -nums[i]
        while j < k:
            local_sum = nums[j] + nums[k]
            if local_sum == target:
                result.append([nums[i], nums[j], nums[k]])
                # Move both pointers to skip duplicates
                while j < k and nums[j] == nums[j + 1]:
                    j += 1
                while j < k and nums[k] == nums[k - 1]:
                    k -= 1
                j += 1
                k -= 1
            elif local_sum < target:
                j += 1
            else:  # local_sum > target
                k -= 1

    return result


            


        
        
        





        
        

        
        
        
        
       
        

    

            
            
            
                            

        
       

