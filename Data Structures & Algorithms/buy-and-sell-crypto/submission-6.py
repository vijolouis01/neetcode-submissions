class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_price = 0

        for price in prices:

            if price < min_price:
                min_price = price
            if max_price < price - min_price:
                max_price = price - min_price    
        return max_price    