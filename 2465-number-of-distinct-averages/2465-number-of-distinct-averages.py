class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        left  = 0
        right = len(nums)-1
        average_list = []

        while(left<right):
            a = nums[left]
            b = nums[right]
            c = float((a+b)/2)
            if c not in average_list:
                average_list.append(c)

            left+=1
            right-=1
        
        return (len(average_list))