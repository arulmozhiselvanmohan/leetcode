class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        s_nums = list(set(nums))
        s_nums.sort(reverse=True)

        if len(s_nums)==1:
            return s_nums[0]
        elif len(s_nums)==2:
            return s_nums[0]
        else:
            return s_nums[2]
        