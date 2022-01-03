class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        left = 0
        right = 0
        
        while right < len(nums)-1:
            max_len = 0
            for i in range(left, right+1):
                max_len = max(max_len, i+nums[i])
            left = right + 1
            right = max_len
            jumps += 1
            
        return jumps
            
