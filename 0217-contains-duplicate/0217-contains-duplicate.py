class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

    ##Create a set of nums that will eliminate duplicates
    ##If we compare the length between created set and the numbers, its easier to find the duplicates
        return (len(set(nums))< len(nums))
      
       
        
        
     