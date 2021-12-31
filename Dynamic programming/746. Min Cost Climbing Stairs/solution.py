class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        last = cost[-1]
        second_last = cost[-2]
        
        for i in range(len(cost)-3, -1, -1):
            f1 = cost[i] + min(last, second_last)
            last = second_last
            second_last = f1
            
        return min(last, second_last)
    
