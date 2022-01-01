class Solution:
    def rob_util(self, nums: List[int]) -> int:
        print(nums)
        if len(nums) < 3:
            return max(nums)
        
        comp_arr = [0] * len(nums)
        comp_arr[-1], comp_arr[-2] = nums[-1], nums[-2]
        comp_arr[-3] = nums[-3] + comp_arr[-1]        
        
        for i in range(len(nums)-4, -1, -1):
            curr_max = nums[i] + max(comp_arr[i+2], comp_arr[i+3])
            comp_arr[i] = curr_max
            
        return max(comp_arr[0], comp_arr[1])
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        
        return max(self.rob_util(nums[0:len(nums)-1]), self.rob_util(nums[1:len(nums)]))
        
