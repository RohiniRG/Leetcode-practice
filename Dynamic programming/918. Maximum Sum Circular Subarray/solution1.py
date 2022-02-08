class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if max(nums) <= 0: 
            return max(nums)
        
        endmax = nums
        endmin = nums
        
        for i in range(1,len(nums)):
            if endmax[i-1] > 0: 
                endmax[i] += endmax[i-1]
                
            if endmin[i-1] < 0: 
                endmin[i] += endmin[i-1]

        return max(max(endmax), sum(nums)-min(endmin))
            
