class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        profit = 0
        for price in prices:
            if min_price > price:
                min_price = price

            if price - min_price > profit:
                profit = price - min_price
        return profit        