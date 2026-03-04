class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        if len(nums)==0:
            return [0]
        
        convert_set = set(nums)
        res = []

        for i in range(1,len(nums)+1):
            if i not in convert_set:
                res.append(i)
        
        return res
        
        