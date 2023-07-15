class Solution:
    def maxProfit(self, prices) -> int:
        lowest = prices[0]
        profit = 0

        for price in prices:
            if lowest > price:
                lowest = price
            profit = max(profit, price - lowest)

        return profit