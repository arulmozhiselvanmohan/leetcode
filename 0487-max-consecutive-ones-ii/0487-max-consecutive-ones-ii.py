class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        left = 0
        max_count = 0
        zero_count = 0  # number of zeros in the current window

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            # shrink window until at most one zero
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # update max_count
            max_count = max(max_count, right - left + 1)

        return max_count