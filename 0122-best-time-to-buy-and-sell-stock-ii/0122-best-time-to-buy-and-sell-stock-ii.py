class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def maxProfit(self, prices: List[int]) -> int:
        l = 0
        n = len(prices)
        stock_total = 0

        while l < n - 1:
            r = l + 1
            day_total = 0

            # Find increasing sequence
            while r < n and prices[r] >= prices[r - 1]:
                day_total = prices[r] - prices[l]
                r += 1

            stock_total += day_total
            l = r  # move buy pointer forward

        return stock_total
            
