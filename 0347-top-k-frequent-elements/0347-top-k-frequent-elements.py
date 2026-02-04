class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequency_counters = Counter(nums)
        items = frequency_counters.items()

        sorted_items = sorted(items, key=lambda x: x[1], reverse=True)

        return [result[0] for result in sorted_items[:k]]



        