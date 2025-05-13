class Solution:
    
    def removeDuplicates(self, nums: List[int]) -> int:
        # Edge case: If the list is empty, return 0
        if not nums:
            return 0
        
        # Initialize two pointers
        i = 0  # Pointer for the last unique element
        
        # Start with j from the second element
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:  # When a new unique element is found
                i += 1  # Move the pointer for unique elements
                nums[i] = nums[j]  # Place the new unique element at the correct position
        
        # The length of unique elements will be i + 1
        return i + 1
        



     
        
       



        

        