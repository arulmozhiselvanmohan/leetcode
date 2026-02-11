class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        nums_table = Counter(nums)
        result= []
        ref = len(nums)/3

        for key, value in nums_table.items():
            if value > ref:
                result.append(key)
        
        return result
        