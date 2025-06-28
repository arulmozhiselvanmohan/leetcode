class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        num_map = {}

        for i,num in enumerate(numbers):
            remaining = target-num
            if remaining in num_map:
                return [num_map[remaining]+1,i+1]
            num_map[num] = i
     
