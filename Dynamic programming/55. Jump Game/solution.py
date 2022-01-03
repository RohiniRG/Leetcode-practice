class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums)-1
        
        for i in range(len(nums)-2, -1, -1):
            if last - i <= nums[i]:
                last = i
        
        if last == 0:
            return True
        else:
            return False
        
