class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      input_set = {} 

      for num in nums:
        if num in input_set:
            input_set[num] += 1
        else:
            input_set[num] = 1
    
      frequency = list(input_set.values())

      frequency.sort(reverse=True)

      if frequency[0] > 1:
        return True
      else:
        return False       