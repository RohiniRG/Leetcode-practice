class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -100000
        recent = 0
        for i in nums:
            recent += i
            if recent > max_sum:
                max_sum = recent
                
            if recent < 0:
                recent = 0
                
        return max_sum
            
