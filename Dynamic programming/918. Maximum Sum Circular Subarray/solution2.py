class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        
        currSum = 0
        
        maxSum = nums[0]
        minSum = nums[0]
        
        currMax = 0
        currMin = 0
        
        for n in nums:
            currSum += n
            
            currMax = max(n, currMax+n)
            maxSum = max(currMax, maxSum)
            
            currMin = min(n, currMin+n)
            minSum = min(currMin, minSum)
            
        
        if maxSum > 0: 
            return max(maxSum, currSum-minSum)
        else:
            return(maxSum)
        
 
