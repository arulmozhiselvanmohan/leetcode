class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        nums_table = Counter(nums)
        result= []

        for key, value in nums_table.items():
            if value > len(nums)/3:
                result.append(key)
        
        return result
        