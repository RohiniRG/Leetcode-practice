class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = 0
        cool = 0
        buy = -10000000
        for price in prices:
            prev_sell = sell
            sell = max(sell, buy + price)
            buy = max(buy, cool - price)
            cool = prev_sell
        
        return sell

