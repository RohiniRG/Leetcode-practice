class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        
        prefix = 1
        for i in range(len(nums)):
            ans.append(prefix)
            prefix *= nums[i]
            
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]
            
        return ans
        
