class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        def getProduct(last3):
            return last3[0] * last3[1] * last3[2]
            
        if len(nums) == 3:
            return getProduct(nums)
        
        nums = sorted(nums)
        return max(getProduct([nums[-1], nums[0], nums[1]]), getProduct(nums[len(nums)-1: len(nums)-4: -1]))
    
