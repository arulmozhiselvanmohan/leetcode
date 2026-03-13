class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        # Counts for sliding window
        max_count = 0
        count = 0        # current window length
        prev_count = 0   # consecutive ones before the flipped zero
        zero_used = False

        for num in nums:
            if num == 1:
                count += 1
            else:  # num == 0
                if not zero_used:
                    count += 1  # flip this zero
                    zero_used = True
                else:
                    # reset window: count = ones after previous zero + 1 (flip this zero)
                    count = prev_count + 1
                    zero_used = True
                # update prev_count to consecutive ones before this zero
                prev_count = 0
            if num == 1:
                prev_count += 1
            else:
                prev_count = 0
            max_count = max(max_count, count)

        return max_count