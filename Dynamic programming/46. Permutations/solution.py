class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        
        result_lists = self.permute(nums[1:])
        ans = []
        
        for each_list in result_lists:
            for i in range(len(each_list)+1):
                temp_list = each_list.copy()
                temp_list.insert(i, nums[0])
                ans.append(temp_list)
                
        return ans

