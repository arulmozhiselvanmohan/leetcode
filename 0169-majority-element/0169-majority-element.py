class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_val = len(nums)/2

        dict_list = Counter(nums)

        max_key = max(dict_list, key=dict_list.get)

        return max_key
        