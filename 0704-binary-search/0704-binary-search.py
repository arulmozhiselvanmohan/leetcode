class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums.sort()
        a,b=0,len(nums)-1
    
        while a<=b:
            k = int((a+b)/2)
            if(nums[k]==target):
                return k
            if(nums[k]>target):
                b=k-1
            else:
                a=k+1
        
        return -1
        