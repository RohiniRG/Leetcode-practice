class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        min_day = prices[0]
        
        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[i]-min_day)
            min_day = min(prices[i], min_day)
            
        return maxProfit

