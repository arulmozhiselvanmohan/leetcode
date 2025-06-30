class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        for num in range(1,len(nums)):
            if abs(nums[num]) < abs(closest) or (abs(nums[num]) == abs(closest) and nums[num] > closest):
                closest = nums[num]
        return closest







        