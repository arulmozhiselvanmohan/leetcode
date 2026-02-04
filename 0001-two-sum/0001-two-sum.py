class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

            hash_map = {}
            
            for index, number in  enumerate(nums):
                remaining = target - number
                if remaining in hash_map:
                    return [hash_map[remaining],index]
                else:
                    hash_map[number] = index
       