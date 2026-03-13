class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        window = {}

        for i in range(len(nums)):
            if nums[i] in window:
                if i-window[nums[i]] <=k:
                    return True
            window[nums[i]]=i

        return False
        